from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.CostWork.forms import CostWorkForm
from core.CostWork.models import CostWork


def cost_work_list(request):
    cost_works = CostWork.objects.all().order_by('id')
    return render(request, 'CostWork/cost_work_list.html',
                  {'cost_works': cost_works})


def cost_work_detail(request, cost_work_id):
    cost_work = get_object_or_404(CostWork, pk=cost_work_id)
    return render(request, 'CostWork/cost_work_detail.html',
                  {'cost_work': cost_work})


def cost_work_add(request):
    if request.method == "POST":
        form = CostWorkForm(request.POST)
        if form.is_valid():
            cost_work = form.save(commit=False)
            cost_work.analysis = form.cleaned_data['analysis']
            cost_work.work = form.cleaned_data['work']
            cost_work.process = form.cleaned_data['process']
            cost_work.cost_work = form.cleaned_data['cost_work']
            cost_work.kind = form.cleaned_data['kind']
            cost_work.duration = form.cleaned_data['duration']
            cost_work.measure = form.cleaned_data['measure']
            cost_work.save()
            return redirect('cost_work-list')
    else:
        form = CostWorkForm()
    return render(request, 'CostWork/cost_work_add.html',
                  {'form': form})


def cost_work_edit(request, cost_work_id):
    cost_work = get_object_or_404(CostWork, pk=cost_work_id)
    if request.method == "POST":
        form = CostWorkForm(request.POST, instance=cost_work)
        if form.is_valid():
            cost_work = form.save(commit=False)
            cost_work.analysis = form.cleaned_data['analysis']
            cost_work.work = form.cleaned_data['work']
            cost_work.process = form.cleaned_data['process']
            cost_work.cost_work = form.cleaned_data['cost_work']
            cost_work.kind = form.cleaned_data['kind']
            cost_work.duration = form.cleaned_data['duration']
            cost_work.measure = form.cleaned_data['measure']
            cost_work.save()
            return redirect('cost_work-list')
    else:
        form = CostWorkForm(instance=cost_work)
    return render(request, 'CostWork/cost_work_edit.html',
                  {'form': form})


def cost_work_delete(request, cost_work_id):
    cost_work = get_object_or_404(CostWork, pk=cost_work_id)
    try:
        cost_work.delete()
    except ProtectedError:
        messages.warning(request, _('Analysis cost has related objects and can not be deleted'))
    return redirect('cost_work-list')
