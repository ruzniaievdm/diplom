from django.contrib import messages
from django.db import transaction
from django.db.models import ProtectedError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from Manager.BusinessProcess.forms import BusinessProcessForm
from core.BusinessProcess.models import BusinessProcess
from core.BusinessProcessWork.models import BusinessProcessWork


def bp_list(request):
    bps = BusinessProcess.objects.all().order_by('id')
    context = {'bps': bps, }
    return render(request, 'BusinessProcess/bp_list.html',
                  context)


def bp_detail(request, bp_id):
    bp = get_object_or_404(BusinessProcess, pk=bp_id)
    bpworks = BusinessProcessWork.objects.all().filter(process_id=bp)
    return render(request, 'BusinessProcess/bp_detail.html',
                  {'bp': bp, 'bpworks': bpworks})


def bp_expenses(request, bp_id):
    bp = get_object_or_404(BusinessProcess, pk=bp_id)
    bpworks = BusinessProcessWork.objects.all().filter(process_id=bp)
    context = {'bp': bp, 'bpworks': bpworks}
    return render(request, 'BusinessProcess/bp_expenses.html', context)


def bp_add(request):
    if request.method == "POST":
        form = BusinessProcessForm(request.POST)
        if form.is_valid():
            bp = form.save(commit=False)
            bp.name = form.cleaned_data['name']
            bp.enterprise = form.cleaned_data['enterprise']
            bp.bp_group = form.cleaned_data['bp_group']
            bp.save()
            return redirect('bp-list')
    else:
        form = BusinessProcessForm()
    return render(request, 'BusinessProcess/bp_add.html',
                  {'form': form})
    #
    # process = BusinessProcess.objects.get(pk=bp_id)
    # if request.method == "POST":
    #     formset = BusinessProcessWorkFormSet(request.POST, instanse=process)
    #     if formset.is_valid():
    #         formset.save()
    #         return redirect('bp-list')
    # else:
    #     formset = BusinessProcessWorkFormSet(instance=process)
    # return render(request, 'BusinessProcess/bp_add.html', {
    #     'formset': formset,
    # })


def bp_edit(request, bp_id):
    bp = get_object_or_404(BusinessProcess, pk=bp_id)
    if request.method == "POST":
        form = BusinessProcessForm(request.POST, instance=bp)
        if form.is_valid():
            bp = form.save(commit=False)
            bp.name = form.cleaned_data['name']
            bp.cost_plan = form.cleaned_data['cost_plan']
            bp.relative_important = form.cleaned_data['relative_important']
            bp.enterprise = form.cleaned_data['enterprise']
            bp.bp_group = form.cleaned_data['bp_group']
            bp.save()
            return redirect('bp-list')
    else:
        form = BusinessProcessForm(instance=bp)
    return render(request, 'BusinessProcess/bp_edit.html',
                  {'form': form})


def bp_delete(request, bp_id):
    bp = get_object_or_404(BusinessProcess, pk=bp_id)
    try:
        bp.delete()
    except ProtectedError:
        messages.warning(request, _('Business process has related objects and can not be deleted'))
    return HttpResponse("Deleted!")
