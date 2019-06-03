from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.Department.forms import DepartmentForm
from core.Department.models import Department


def department_list(request):
    departments = Department.objects.all().order_by('id')
    return render(request, 'Department/department_list.html',
                  {'departments': departments})


def department_add(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.name = form.cleaned_data['name']
            department.enterprise = form.cleaned_data['enterprise']
            department.save()
            print(form.cleaned_data)
            print(department)
            print(form.cleaned_data)
            messages.success(request, "Added")
            return redirect('department-list')
    else:
        form = DepartmentForm()
    return render(request, 'Department/department_add.html',
                  {'form': form})


def department_edit(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            department = form.save(commit=False)
            department.name = form.cleaned_data['name']
            department.enterprise = form.cleaned_data['enterprise']
            department.save()
            return redirect('department-list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'Department/department_edit.html',
                  {'form': form})


def department_delete(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    try:
        department.delete()
    except ProtectedError:
        messages.warning(request, _('Department has related objects and can not be deleted'))
    return redirect('department-list')
