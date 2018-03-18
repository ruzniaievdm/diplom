import datetime
from django import forms
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from core.Analysis.models import Analysis


class AnalysisForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = ('description',)

    description = forms.CharField(
        max_length=128, label=_('Описание'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Analysis description'),
                   'class': 'form-control', 'type': 'text', }))

    #create_at = forms.DateTimeField(initial=datetime.time)
