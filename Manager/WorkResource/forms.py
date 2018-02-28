from django import forms
from django.utils.translation import ugettext_lazy as _

from core.BusinessProcessWork.models import BusinessProcessWork
from core.Resource.models import Resource
from core.WorkResource.models import WorkResource


class WorkResourceForm(forms.ModelForm):
    class Meta:
        model = WorkResource
        fields = '__all__'

    work = forms.ModelChoiceField(queryset=BusinessProcessWork.objects.all(), empty_label=None, label=_('Работа'),
                                  widget=forms.Select(attrs={'id': 'work', 'class': 'form-control'}))

    resource = forms.ModelChoiceField(queryset=Resource.objects.all(), empty_label=None,
                                      label=_('Ресурсы'),
                                      widget=forms.Select(
                                          attrs={'id': 'resource', 'class': 'form-control'}))

    expense = forms.FloatField(required=True, max_value=1000000, label=_('Расход'), min_value=1,
                               widget=forms.NumberInput(
                                   attrs={'id': 'expense', 'placeholder': _('Expense'),
                                          'class': 'form-control', }), )
