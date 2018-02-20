from typing import re
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views import generic
from .forms import *


def index(request):
    num_enterprise = Enterprise.objects.all().count()
    num_businessProcess = BusinessProcess.objects.all().count()
    return render(request, 'app/index.html',
                  context={'num_enterprise': num_enterprise, 'num_businessProcess': num_businessProcess})


def business_proceses(request):
    business_proceses = BusinessProcess.objects.all()
    return render(request, 'app/business_process_list.html', {'business_proceses': business_proceses})


def business_process_detail(request, id):
    business_process = get_object_or_404(BusinessProcess, pk=id)
    return render(request, 'app/business_process_detail.html', {'business_process': business_process})


'''
INDICATOR AND ANALYSIS
'''  # def analysis_form(request):


#     #form = AnalysisForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.save()
#         else:
#             form = Analysis()
#     return render(request, 'app/analysis_list.html', {'form': form})


def analysis_list(request):
    analysis = Analysis.objects.all()
    return render(request, 'app/analysis_list.html', {'analysis': analysis})
