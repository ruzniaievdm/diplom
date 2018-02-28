from django import forms
from django.utils.translation import ugettext_lazy as _

from core.ScaleMeasure.models import ScaleMeasure
from core.UnitMeasure.models import UnitMeasure


class UnitMeasureForm(forms.ModelForm):
    class Meta:
        model = UnitMeasure
        fields = '__all__'

    name = forms.CharField(
        max_length=16, label=_('Название'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Unit name'),
                   'class': 'form-control', 'type': 'text', }))

    scale = forms.ModelChoiceField(queryset=ScaleMeasure.objects.all(), empty_label=None,
                                   label='Шкала измерений', widget=forms.Select(
            attrs={'id': 'scale', 'class': 'form-control'}), )

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = ScaleMeasure.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Scale with name %(name)s already exists'), params={'name': name},
                                        code='invalid')
        # raise forms.ValidationError(self.error_messages['password_mismatch'])
        return name

        # error_messages = {
        #     'password_mismatch': _("The two password fields didn't match."),
        # }
