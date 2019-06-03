from django import forms
from django.forms import BaseFormSet, formset_factory
from django.utils.translation import ugettext_lazy as _

from core.AnalysisProcess.models import AnalysisProcess
from core.ArrowWorks.models import ArrowWorks
from core.BusinessProcessWork.models import BusinessProcessWork
from core.CostWorks.models import CostWorks
from core.GlossaryArrow.models import GlossaryArrow
from core.ImportanceWorks.models import ImportanceWorks


class ArrowWorksForm(forms.ModelForm):
    class Meta:
        model = ArrowWorks
        fields = '__all__'

    arrow = forms.ModelChoiceField(queryset=GlossaryArrow.objects.all(), empty_label=None, required=False,
                                   label=_('Стрелка работы'), to_field_name='id',
                                   widget=forms.Select(attrs={'id': 'arrow', 'class': 'form-control'}))

    work = forms.ModelChoiceField(queryset=BusinessProcessWork.objects.all(), empty_label=None, required=False,
                                  label=_('Работа БП'),
                                  widget=forms.Select(attrs={'id': 'work', 'class': 'form-control'}))

    description = forms.CharField(label=_('Описание'),
                                  required=False,
                                  widget=forms.TextInput(
                                      attrs={'id': 'description',
                                             'placeholder': _('Description'),
                                             'class': 'form-control', }), )

    def clean_name(self):
        arrow = self.cleaned_data['arrow']
        work = self.cleaned_data['work']
        qs = ArrowWorks.objects.filter(arrow=arrow, work=work)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_(
                'Arrow works with this work already exists, create new analysis'))

