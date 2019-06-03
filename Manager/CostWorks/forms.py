from django import forms
from django.forms import BaseFormSet, formset_factory
from django.utils.translation import ugettext_lazy as _

from core.AnalysisProcess.models import AnalysisProcess
from core.BusinessProcessWork.models import BusinessProcessWork
from core.CostWorks.models import CostWorks


class CostWorksAnalysisForm(forms.ModelForm):
    class Meta:
        model = CostWorks
        fields = '__all__'

    unique_cw = forms.ModelChoiceField(queryset=AnalysisProcess.objects.all(), empty_label=None, required=True,
                                       label=_('Анилиз процессов'), to_field_name='id',
                                       widget=forms.Select(attrs={'id': 'analysis_process', 'class': 'form-control'}))

    work = forms.ModelChoiceField(queryset=BusinessProcessWork.objects.all(), empty_label=None, required=False,
                                  label=_('Работа БП'),
                                  widget=forms.Select(attrs={'id': 'work', 'class': 'form-control'}))

    kind = forms.CharField(max_length=64, label=_('Вид функции'), widget=forms.TextInput(
        attrs={'id': 'kind', 'placeholder': _('Kind work'),
               'class': 'form-control', 'type': 'text', }))

    cost_work = forms.FloatField(max_value=100000, label=_('Cтоимость работы'),
                                 min_value=1,
                                 widget=forms.NumberInput(
                                     attrs={'id': 'cost_work', 'placeholder': _('Сost work'),
                                            'class': 'form-control', }), )

    duration = forms.FloatField(max_value=1000, label=_('Продолжительность работы, часы'),
                                min_value=1,
                                widget=forms.NumberInput(
                                    attrs={'id': 'duration', 'placeholder': _('Duration'),
                                           'class': 'form-control', }), )

    # def clean_name(self):
    #     unique_cw = self.cleaned_data['unique_cw']
    #     work = self.cleaned_data['work']
    #     qs = CostWorks.objects.filter(unique_cw=unique_cw, work=work)
    #     if qs.exists() and self.instance:
    #         qs.exclude(pk=self.instance.pk)
    #     if qs.exists():
    #         raise forms.ValidationError(_(
    #             'Analysis process with this work already exists, create new analysis'))


class BaseCostWorksFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        works = []
        for form in self.forms:
            work = form.cleaned_data['work']
            if work in works:
                raise forms.ValidationError('wo')
        works.append(work)


CostWorksAnalysisFormSet = formset_factory(CostWorksAnalysisForm, formset=BaseCostWorksFormSet, extra=1)
