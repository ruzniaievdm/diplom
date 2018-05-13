from django import forms
from django.forms import BaseFormSet, formset_factory, inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from core.BusinessProcess.models import BusinessProcess
from core.BusinessProcessWork.models import BusinessProcessWork


class BusinessProcessWorkForm(forms.ModelForm):
    process = forms.ModelChoiceField(
        queryset=BusinessProcess.objects.all(), empty_label=None,
        label='Бизнес-процесс', widget=forms.Select(
            attrs={'id': 'bp', 'class': 'form-control'}))

    level = forms.ChoiceField(
        choices=BusinessProcessWork.level_of_choices,
        label=_('Уровень работы'), widget=forms.Select(
            attrs={'id': 'level', 'class': 'form-control'}))

    parent = forms.ModelChoiceField(
        queryset=BusinessProcessWork.objects.all(), empty_label='', required=False,
        label=_('Родительская работа'),
        widget=forms.Select(
            attrs={'id': 'parent', 'class': 'form-control', }))

    name = forms.CharField(
        max_length=128, label=_('Название'), widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': _('Name'),
                   'class': 'form-control', 'type': 'text', }))

    class Meta:
        model = BusinessProcessWork
        fields = ['process', 'level', 'parent', 'name']

    def clean_parent(self):
        parent = self.cleaned_data['parent']
        level = int(self.cleaned_data['level'])
        bp_level = int(BusinessProcessWork.level_of_choices[0][0])
        if not parent:
            if level != bp_level:
                raise forms.ValidationError(_('This field is required if level is not 1. Choose parent!'))
        return parent

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = BusinessProcessWork.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                _('Work with name %(name)s already exists'), params={'name': name})
        return name

# class BusinessProcessWorkForm(forms.ModelForm):
#     class Meta:
#         model = BusinessProcessWork
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(BusinessProcessWorkForm, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({'class': 'form-control'})
#
#
# class BaseBusinessProcessWorkFormSet(BaseFormSet):
#     def clean_parent(self):
#         parent = self.cleaned_data['parent']
#         level = int(self.cleaned_data['level'])
#         bp_level = int(BusinessProcessWork.level_of_choices[0][0])
#         if not parent:
#             if level != bp_level:
#                 raise forms.ValidationError(_('This field is required if level is not 1. Choose parent!'))
#         return parent
#
#     def clean_name(self):
#         name = self.cleaned_data['name']
#         process = self.cleaned_data['process']
#         qs = BusinessProcessWork.objects.filter(name=name, process=process)
#         if qs.exists() and self.instance:
#             qs.exclude(pk=self.instance.pk)
#         if qs.exists():
#             raise forms.ValidationError(
#                 _('Work with name %(name)s already exists'), params={'name': name})
#         return name
#
#
# BusinessProcessWorkFormSet = inlineformset_factory(BusinessProcess, BusinessProcessWork,
#                                                    fk_name='process', fields=('name', 'level', 'parent', 'process'),widgets={'name':TextArea()})
#
