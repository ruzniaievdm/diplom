from django import forms
from django.utils.translation import ugettext_lazy as _

from core.ArrowType.models import ArrowType


class ArrowTypeForm(forms.ModelForm):
    class Meta:
        model = ArrowType
        fields = '__all__'

    name = forms.CharField(
        max_length=32, label=_('Название'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Type'),
                   'class': 'form-control', 'type': 'text', }))

    short_name = forms.CharField(
        max_length=1, label=_('Название(сокращенно)'), widget=forms.TextInput(
            attrs={'id': 'names', 'required': True,
                   'placeholder': _('Type short'),
                   'class': 'form-control', 'type': 'text', }))

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = ArrowType.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Type with name %(name)s already exists'), params={'name': name})
        return name
