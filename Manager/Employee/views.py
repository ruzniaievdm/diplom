from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.Employee.forms import EmployeeForm
from core.Employee.models import Employee


def employee_list(request):
    employees = Employee.objects.all().order_by('id')
    return render(request, 'Employee/employee_list.html',
                  {'employees': employees})


def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'Employee/employee_detail.html',
                  {'employee': employee})


def employee_add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.first_name = form.cleaned_data['first_name']
            employee.last_name = form.cleaned_data['last_name']
            employee.patronymic = form.cleaned_data['patronymic']
            employee.department = form.cleaned_data['department']
            employee.position_employee = form.cleaned_data['position_employee']
            employee.save()
            return redirect('employee-detail')
    else:
        form = EmployeeForm()
    return render(request, 'Employee/employee_add.html', {'form': form})


def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            employee = form.save(commit=False)
            employee.first_name = form.cleaned_data['first_name']
            employee.last_name = form.cleaned_data['last_name']
            employee.patronymic = form.cleaned_data['patronymic']
            employee.department = form.cleaned_data['department']
            employee.position_employee = form.cleaned_data['position_employee']
            employee.save()
            return redirect('employee-list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'Employee/employee_edit.html', {'form': form})


def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    try:
        employee.delete()
    except ProtectedError:
        messages.warning(request, 'Employee has related objects and can not be deleted')
    return redirect('employee-list')
