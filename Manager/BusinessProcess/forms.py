from django import forms
from django.utils.translation import ugettext_lazy as _

from core.BusinessProcess.models import BusinessProcess
from core.Enterprise.models import Enterprise
from core.BusinessProcessGroup.models import BusinessProcessGroup


class BusinessProcessForm(forms.ModelForm):
    class Meta:
        model = BusinessProcess
        fields = '__all__'

    name = forms.CharField(
        max_length=128, label=_('Название'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Business process name'),
                   'class': 'form-control', 'type': 'text', }))

    cost_plan = forms.DecimalField(required=True, max_value=1000000, label=_('Плановая стоимость'), min_value=1,
                                   widget=forms.NumberInput(
                                       attrs={'id': 'cost_plan', 'placeholder': _('Сost plan'),
                                              'class': 'form-control', }), )

    relative_important = forms.FloatField(required=True, max_value=1, label=_('Относительная важность'),
                                          min_value=0.001,
                                          widget=forms.NumberInput(
                                              attrs={'id': 'relative_important', 'placeholder': _('Relative important'),
                                                     'class': 'form-control', 'step': "0.001"}))

    enterprise = forms.ModelChoiceField(queryset=Enterprise.objects.all(), empty_label=None,
                                        label='Предприятие', widget=forms.Select(
            attrs={'id': 'enterprise', 'class': 'form-control'}), )

    bp_group = forms.ModelChoiceField(queryset=BusinessProcessGroup.objects.all(), empty_label=None,
                                      label='Группа бизнес-процесса', widget=forms.Select(
            attrs={'id': 'enterprise', 'class': 'form-control'}), )

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = BusinessProcess.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Business process %s already exists' % name))
            return name
