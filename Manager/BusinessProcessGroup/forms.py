from django import forms
from django.utils.translation import ugettext_lazy as _

from core.BusinessProcessGroup.models import BusinessProcessGroup


class BusinessProcessGroupForm(forms.ModelForm):
    class Meta:
        model = BusinessProcessGroup
        fields = '__all__'

    name = forms.CharField(
        max_length=64, label=_('Название'), widget=forms.TextInput(
            attrs={'id': 'id_name', 'required': True,
                   'placeholder': _('Business process group name'),
                   'class': 'form-control', 'type': 'text', }))

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = BusinessProcessGroup.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Business process group with this name already exists'))
        return name
