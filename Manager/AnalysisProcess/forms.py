from django import forms
from django.forms import BaseFormSet, formset_factory
from django.utils.translation import ugettext_lazy as _

from core.Analysis.models import Analysis
from core.AnalysisProcess.models import AnalysisProcess
from core.BusinessProcess.models import BusinessProcess


class AnalysisProcessForm(forms.ModelForm):
    class Meta:
        model = AnalysisProcess
        fields = '__all__'

    analysis = forms.ModelChoiceField(queryset=Analysis.objects.all(), empty_label=None, label=_('Анализ'),
                                      widget=forms.Select(attrs={'id': 'analysis', 'class': 'form-control'}))

    process = forms.ModelChoiceField(queryset=BusinessProcess.objects.all(), empty_label=None,
                                     label=_('Бизнес процесс'),
                                     widget=forms.Select(attrs={'id': 'process', 'class': 'form-control'}))

    is_active_cost = forms.BooleanField(widget=forms.HiddenInput(), required=False)

    is_active_importance = forms.BooleanField(widget=forms.HiddenInput(), required=False)

    def clean_unique(self):
        analysis = self.cleaned_data['analysis']
        process = self.cleaned_data['process']
        qs = AnalysisProcess.objects.filter(analysis=analysis, process=process)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Analysis with this process already exists, create new analysis'))


# class BaseAnalysisProcessFormSet(BaseFormSet):
#     def clean(self):
#         if any(self.errors):
#             return
#         works = []
#         for form in self.forms:
#             work = form.cleaned_data['work']
#             if work in works:
#                 raise forms.ValidationError('wo')
#         works.append(work)
#
#
# AnalysisProcessFormSet = formset_factory(AnalysisProcessForm, formset=BaseAnalysisProcessFormSet, extra=1)
# formset = AnalysisProcessForm()
