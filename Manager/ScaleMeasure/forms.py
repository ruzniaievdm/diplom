from django import forms
from django.utils.translation import ugettext_lazy as _

from core.ScaleMeasure.models import ScaleMeasure


class ScaleMeasureForm(forms.ModelForm):
    class Meta:
        model = ScaleMeasure
        fields = '__all__'

    name = forms.CharField(
        max_length=32, label=_('Название'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Scale measure'),
                   'class': 'form-control', 'type': 'text', }))

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = ScaleMeasure.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Scale with name %(name)s already exists'),
                                        params={'name': name})
        return name
