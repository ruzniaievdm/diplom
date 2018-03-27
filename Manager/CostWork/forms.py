from django import forms
from django.forms import BaseFormSet, formset_factory
from django.utils.translation import ugettext_lazy as _

from core.Analysis.models import Analysis
from core.BusinessProcess.models import BusinessProcess
from core.BusinessProcessWork.models import BusinessProcessWork
from core.CostWork.models import CostWork, Coefficient
from core.UnitMeasure.models import UnitMeasure


class CostWorkForm(forms.ModelForm):
    class Meta:
        model = CostWork
        fields = ['analysis', 'process']

    analysis = forms.ModelChoiceField(queryset=Analysis.objects.all(), empty_label=None, label=_('Анализ'),
                                      widget=forms.Select(attrs={'id': 'analysis', 'class': 'form-control'}))

    process = forms.ModelChoiceField(queryset=BusinessProcess.objects.all(), empty_label=None,
                                     label=_('Бизнес процесс'),
                                     widget=forms.Select(attrs={'id': 'process', 'class': 'form-control'}))

    work = forms.ModelChoiceField(queryset=BusinessProcessWork.objects.all(), empty_label=None,
                                  label=_('Работа БП'),
                                  widget=forms.Select(attrs={'id': 'work', 'class': 'form-control'}))

    measure = forms.ModelChoiceField(queryset=UnitMeasure.objects.all(), empty_label=None,
                                     label=_('Единицы измерений'),
                                     widget=forms.Select(attrs={'id': 'measure', 'class': 'form-control'}))

    kind = forms.CharField(max_length=64, label=_('Вид функции'), widget=forms.TextInput(
        attrs={'id': 'kind', 'required': True,
               'placeholder': _('Kind work'),
               'class': 'form-control', 'type': 'text', }))

    cost_work = forms.FloatField(required=True, max_value=100000, label=_('Cтоимость работы'), min_value=1,
                                 widget=forms.NumberInput(
                                     attrs={'id': 'cost_work', 'placeholder': _('Сost work'),
                                            'class': 'form-control', }), )

    duration = forms.FloatField(required=True, max_value=1000, label=_('Продолжительность работы, часы'), min_value=1,
                                widget=forms.NumberInput(
                                    attrs={'id': 'duration', 'placeholder': _('Duration'),
                                           'class': 'form-control', }), )

    def clean_name(self):
        # work = self.cleaned_data['work']
        analysis = self.cleaned_data['analysis']
        process = self.cleaned_data['process']
        qs = CostWork.objects.filter(analysis=analysis, process=process)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Analysis with this process already exists, create new analysis'))


class CoefficientForm(forms.ModelForm):
    class Meta:
        model = Coefficient
        fields = ['name', 'value']

    def __init__(self, *args, **kwargs):
        super(CoefficientForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class BaseCoefficientFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        names = []
        for form in self.forms:
            name = form.cleaned_data['name']
            if name in names:
                raise forms.ValidationError('Coefficients in a set must have distinct names.')
            names.append(name)


CoefficientFormSet = formset_factory(CoefficientForm, formset=BaseCoefficientFormSet, extra=7)
