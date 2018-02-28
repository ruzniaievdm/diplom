from django import forms
from django.utils.translation import ugettext_lazy as _

from core.TypeResource.models import TypeResource


class TypeResourceForm(forms.ModelForm):
    class Meta:
        model = TypeResource
        fields = '__all__'

    name = forms.CharField(
        max_length=32, label=_('Название'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Name resource type'),
                   'class': 'form-control', 'type': 'text', }))

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = TypeResource.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Type with name %(name)s already exists'),
                                        params={'name': name})
        return name
