from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.BusinessProcess.forms import BusinessProcessForm
from core.BusinessProcess.models import BusinessProcess


def bp_list(request):
    bps = BusinessProcess.objects.all().order_by('id')
    return render(request, 'BusinessProcess/bp_list.html',
                  {'bps': bps})


def bp_detail(request, bp_id):
    bp = get_object_or_404(BusinessProcess, pk=bp_id)
    return render(request, 'BusinessProcess/bp_detail.html',
                  {'bp': bp})


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

    return redirect('bp-list')
