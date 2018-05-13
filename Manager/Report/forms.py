import datetime
from django import forms
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from core.Report.models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('description',)

    description = forms.CharField(
        max_length=128, label=_('Описание'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Recommendation description'),
                   'class': 'form-control', 'type': 'text', }))
