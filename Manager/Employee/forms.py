from django import forms
from django.utils.translation import ugettext_lazy as _

from core.Department.models import Department
from core.Employee.models import Employee
from core.PositionEmployee.models import PositionEmployee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    first_name = forms.CharField(
        max_length=64, label=_('Имя'), widget=forms.TextInput(
            attrs={'id': 'f_name', 'required': True,
                   'placeholder': _('First name'),
                   'class': 'form-control', 'type': 'text', }))

    last_name = forms.CharField(
        max_length=64, label=_('Фамилия'), widget=forms.TextInput(
            attrs={'id': 'l_name', 'required': True,
                   'placeholder': _('Last name'),
                   'class': 'form-control', 'type': 'text', }))

    patronymic = forms.CharField(
        max_length=64, label=_('Отчество'), widget=forms.TextInput(
            attrs={'id': 'p_name', 'required': True,
                   'placeholder': _('Patronymic'),
                   'class': 'form-control', 'type': 'text', }))

    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label=None,
                                        label='Отдел', widget=forms.Select(
            attrs={'id': 'department', 'class': 'form-control'}), )

    # position = forms.ModelChoiceField(queryset=PositionEmployee.objects.all(), empty_label=None,
    #                                   label='Должность', widget=forms.Select(
    #         attrs={'id': 'position', 'class': 'form-control'}), )

    def clean_name(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        patronymic = self.cleaned_data['patronymic']
        qs = Employee.objects.filter(first_name=first_name, last_name=last_name, patronymic=patronymic)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                _('Employee %s %s %s already exists' % self.first_name, self.last_name, self.patronymic),
                code='invalid')
            return first_name
