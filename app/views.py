from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import generic


def index(request):
    num_enterprise = Enterprise.objects.all().count()
    num_businessProcess = BusinessProcess.objects.all().count()
    return render(request, 'app/index.html',
                  context={'num_enterprise': num_enterprise, 'num_businessProcess': num_businessProcess})


class EnterpriseListView(generic.ListView):
    model = Enterprise


def enterprise_detail(request, id):
    enterprise = get_object_or_404(Enterprise, pk=id)
    return render(request, 'app/enterprise_detail.html', {'enterprise': enterprise})


def business_proceses(request):
    business_proceses = BusinessProcess.objects.all()
    return render(request, 'app/business_process_list.html', {'business_proceses': business_proceses})


def business_process_detail(request, id):
    business_process = get_object_or_404(BusinessProcess, pk=id)
    return render(request, 'app/business_process_detail.html', {'business_process': business_process})
