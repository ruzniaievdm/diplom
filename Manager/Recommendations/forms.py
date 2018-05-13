from django import forms
from django.forms import BaseFormSet, formset_factory
from django.utils.translation import ugettext_lazy as _

from core.AnalysisProcess.models import AnalysisProcess
from core.BusinessProcessWork.models import BusinessProcessWork
from core.Recommendations.models import Recommendations


class RecommendationsForm(forms.ModelForm):
    class Meta:
        model = Recommendations
        fields = '__all__'
        #
        # unique = forms.ModelChoiceField(queryset=AnalysisProcess.objects.all(), empty_label=None, required=True,
        #                                 label=_('Анилиз процессов'), to_field_name='id',
        #                                 widget=forms.Select(attrs={'id': 'analysis_process', 'class': 'form-control'}))
        #
        # work = forms.ModelChoiceField(queryset=BusinessProcessWork.objects.all(), empty_label=None, required=False,
        #                               label=_('Работа БП'),
        #                               widget=forms.Select(attrs={'id': 'work', 'class': 'form-control'}))
        #
        # elemental_importance = forms.FloatField(max_value=1, label=_('Элементная значимость'),
        #                                         min_value=0.000001,
        #                                         widget=forms.NumberInput(
        #                                             attrs={'id': 'importance_works',
        #                                                    'placeholder': _('Elemental importance'),
        #                                                    'class': 'form-control', }), )
        #
        # object_importance = forms.FloatField(max_value=1, label=_('Обьектная значимость'),
        #                                      min_value=0.000001,
        #                                      widget=forms.NumberInput(
        #                                          attrs={'id': 'importance_works', 'placeholder': _('Object importance'),
        #                                                 'class': 'form-control', }), )
        #
        # relative_cost = forms.FloatField(widget=forms.HiddenInput(), required=False)
        #
        # relative_importance = forms.FloatField(widget=forms.HiddenInput(), required=False)

        # def clean_name(self):
        #     unique = self.cleaned_data['unique']
        #     work = self.cleaned_data['work']
        #     qs = CostWorks.objects.filter(unique=unique, work=work)
        #     if qs.exists() and self.instance:
        #         qs.exclude(pk=self.instance.pk)
        #     if qs.exists():
        #         raise forms.ValidationError(_(
        #             'Importance with this work already exists, create new analysis'))
        #
