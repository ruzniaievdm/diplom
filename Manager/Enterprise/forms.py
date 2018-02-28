from django import forms
from django.utils.translation import ugettext_lazy as _

from core.Enterprise.models import Enterprise


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = '__all__'

    name = forms.CharField(
        max_length=128, label=_('Название'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Enterprise name'),
                   'class': 'form-control', 'type': 'text', }))

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = Enterprise.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Enterprise with name %(name)s already exists'), params={'name': name})
        return name
