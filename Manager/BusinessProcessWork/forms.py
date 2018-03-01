from _csv import field_size_limit

from django import forms
from django.utils.translation import ugettext_lazy as _

from core.BusinessProcess.models import BusinessProcess
from core.BusinessProcessWork.models import BusinessProcessWork


class BusinessProcessWorkForm(forms.ModelForm):
    name = forms.CharField(
        max_length=64, label=_('Название'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Name'),
                   'class': 'form-control', 'type': 'text', }))

    level = forms.ChoiceField(
        choices=BusinessProcessWork.level_of_choices,
        label=_('Уровень работы'), widget=forms.Select(
            attrs={'id': 'level', 'class': 'form-control'}))



    parent = forms.ModelChoiceField(
        queryset=BusinessProcessWork.objects.all(), empty_label=None,
        label=_('Родительская работа'), widget=forms.Select(
            attrs={'id': 'parent', 'class': 'form-control'}))

    # parent = forms.CharField(
    #     max_length=64, label=_('Родительская работа'), required=False, widget=forms.TextInput(
    #         attrs={'id': 'parent', 'placeholder': _('Parent work'),
    #                'class': 'form-control', 'type': 'text'}))

    process = forms.ModelChoiceField(
        queryset=BusinessProcess.objects.all(), empty_label=None,
        label='Бизнес-процесс', widget=forms.Select(
            attrs={'id': 'bp', 'class': 'form-control'}))

    class Meta:
        model = BusinessProcessWork
        fields = '__all__'

    # def __init__(self, level, *args, **kwargs):
    #     super(BusinessProcessWorkForm, self).__init__(*args, **kwargs)
    #     self.fields['parent'] = forms.ChoiceField(
    #         choices=[(o.id, str(o)) for o in BusinessProcessWork.objects.filter(level=level)]
    #     )
    def clean_name(self):
        name = self.cleaned_data['name']
        qs = BusinessProcessWork.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                _('Work with name %(name)s already exists'), params={'name': name})
        return name
