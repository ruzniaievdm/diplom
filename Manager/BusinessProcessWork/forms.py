from django import forms
from django.utils.translation import ugettext_lazy as _

from core.BusinessProcess.models import BusinessProcess
from core.BusinessProcessWork.models import BusinessProcessWork


class BusinessProcessWorkForm(forms.ModelForm):
    class Meta:
        model = BusinessProcessWork
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BusinessProcessWorkForm, self).__init__(*args, **kwargs)
        self.fields['parent'].error_messages = {'required': 'custom required message'}

    name = forms.CharField(
        max_length=32, label=_('Название'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Name'),
                   'class': 'form-control', 'type': 'text', }))
    list_of_choices = (
        (1, 'Lvl 1'),
        (2, 'Lvl 2'),
        (3, 'Lvl 3'),
        (4, 'Lvl 4'),
        (5, 'Lvl 5'),
    )
    level = forms.ChoiceField(
        choices=list_of_choices, label=_('Уровень работы'),
        widget=forms.TextInput(attrs={'id': 'level', 'class': 'form-control', }))

    parent = forms.CharField(
        max_length=32, label=_('Родительская работа'), widget=forms.TextInput(
            attrs={'id': 'parent', 'required': False,
                   'placeholder': _('Parent work'),
                   'class': 'form-control', 'type': 'text', }))

    process = forms.ModelChoiceField(
        queryset=BusinessProcess.objects.all(), empty_label=None,
        label='Бизнес-процесс', widget=forms.Select(attrs={'id': 'bp', 'class': 'form-control'}))

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = BusinessProcessWork.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(_('Work with name %(name)s already exists'), params={'name': name})
        return name
