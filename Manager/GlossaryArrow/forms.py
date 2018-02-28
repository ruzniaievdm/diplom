from django import forms
from django.utils.translation import ugettext_lazy as _

from core.ArrowType.models import ArrowType
from core.GlossaryArrow.models import GlossaryArrow


class GlossaryArrowForm(forms.ModelForm):
    class Meta:
        model = GlossaryArrow
        fields = '__all__'

    arrow_description = forms.CharField(
        max_length=64, label=_('Описание'), widget=forms.TextInput(
            attrs={'id': 'description', 'required': True,
                   'placeholder': _('Description arrow'),
                   'class': 'form-control', 'type': 'text', }))

    type = forms.ModelChoiceField(queryset=ArrowType.objects.all(), empty_label=None,
                                  label='Тип стрелки', widget=forms.Select(
            attrs={'id': 'type', 'class': 'form-control'}), )

    def clean_name(self):
        arrow_description = self.cleaned_data['arrow_description']
        qs = ArrowType.objects.filter(arrow_description=arrow_description)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Arrow with description %(arrow_description)s already exists'),
                                        params={'arrow_description': arrow_description})
        return arrow_description
