from django import forms
from django.utils.translation import ugettext_lazy as _

from core.BusinessProcess.models import BusinessProcess
from core.Department.models import Department
from core.Employee.models import Employee
from core.ProcessExecutor.models import ProcessExecutor


class ProcessExecutorForm(forms.ModelForm):
    class Meta:
        model = ProcessExecutor
        fields = '__all__'

    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label=None, label='Отдел',
                                        widget=forms.Select(attrs={'id': 'department', 'class': 'form-control'}))

    business_process = forms.ModelChoiceField(queryset=BusinessProcess.objects.all(), empty_label=None,
                                              label='Бизнес-процесс',
                                              widget=forms.Select(
                                                  attrs={'id': 'business_process', 'class': 'form-control'}))
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label=None,
                                      label='Ответственный отрудник',
                                      widget=forms.Select(attrs={'id': 'employee', 'class': 'form-control'}))


