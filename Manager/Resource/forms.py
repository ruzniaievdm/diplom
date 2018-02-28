from django import forms
from django.utils.translation import ugettext_lazy as _

from core.Department.models import Department
from core.Enterprise.models import Enterprise
from core.Resource.models import Resource
from core.TypeResource.models import TypeResource
from core.UnitMeasure.models import UnitMeasure


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'

    name = forms.CharField(
        max_length=32, label=_('Название'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Resource name'),
                   'class': 'form-control', 'type': 'text', }))

    cost = forms.FloatField(required=True, max_value=1000000, label=_('Cтоимость'), min_value=1,
                            widget=forms.NumberInput(
                                attrs={'id': 'cost', 'placeholder': _('Сost'),
                                       'class': 'form-control', }), )

    type = forms.ModelChoiceField(queryset=TypeResource.objects.all(), empty_label=None,
                                  label='Тип ресурсов', widget=forms.Select(
            attrs={'id': 'type', 'class': 'form-control'}), )

    measure = forms.ModelChoiceField(queryset=UnitMeasure.objects.all(), empty_label=None,
                                     label='Единица измерений', widget=forms.Select(
            attrs={'id': 'measure', 'class': 'form-control'}), )

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = Resource.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Resource with name %(name)s already exists'), params={'name': name},
                                        code='invalid')
        # raise forms.ValidationError(self.error_messages['password_mismatch'])
        return name

        # error_messages = {
        #     'password_mismatch': _("The two password fields didn't match."),
        # }
