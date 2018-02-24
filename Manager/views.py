from typing import re
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from core.BusinessProcess.models import BusinessProcess
from core.BusinessProcessGroup.models import BusinessProcessGroup
from core.Department.models import Department
from core.Employee.models import Employee
from core.Enterprise.models import Enterprise
from core.PositionEmployee.models import PositionEmployee


def index(request):
    num_enterprise = Enterprise.objects.all().count()
    num_bp = BusinessProcess.objects.all().count()
    num_bpgroup = BusinessProcessGroup.objects.all().count()
    num_department = Department.objects.all().count()
    num_position = PositionEmployee.objects.all().count()
    num_employee = Employee.objects.all().count()
    return render(request, 'index.html',
                  context={'num_enterprise': num_enterprise, 'num_bp': num_bp, 'num_bpgroup': num_bpgroup,
                           'num_department': num_department, 'num_position': num_position,
                           'num_employee': num_employee})