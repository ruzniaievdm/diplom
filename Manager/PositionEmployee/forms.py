from django import forms
from django.utils.translation import ugettext_lazy as _

from core.PositionEmployee.models import PositionEmployee


class PositionEmployeeForm(forms.ModelForm):
    class Meta:
        model = PositionEmployee
        fields = '__all__'

    name = forms.CharField(
        max_length=64, label=_('Названиe'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Position employee'),
                   'class': 'form-control', 'type': 'text', }))

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = PositionEmployee.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Position employee with name %s already exists' % name)
        return name
