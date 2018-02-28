from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.UnitMeasure.forms import UnitMeasureForm
from core.UnitMeasure.models import UnitMeasure


def unit_measure_list(request):
    unitms = UnitMeasure.objects.all().order_by('id')
    return render(request, 'UnitMeasure/unitm_list.html',
                  {'unitms': unitms})


def unit_measure_add(request):
    if request.method == "POST":
        form = UnitMeasureForm(request.POST)
        if form.is_valid():
            unitm = form.save(commit=False)
            unitm.name = form.cleaned_data['name']
            unitm.scale = form.cleaned_data['scale']
            unitm.save()
            return redirect('unitm-list')
    else:
        form = UnitMeasureForm()
    return render(request, 'UnitMeasure/unitm_add.html',
                  {'form': form})


def unit_measure_edit(request, unitm_id):
    unitm = get_object_or_404(UnitMeasure, pk=unitm_id)
    if request.method == "POST":
        form = UnitMeasureForm(request.POST, instance=unitm)
        if form.is_valid():
            unitm = form.save(commit=False)
            unitm.name = form.cleaned_data['name']
            unitm.scale = form.cleaned_data['scale']
            unitm.save()
            return redirect('unitm-list')
    else:
        form = UnitMeasureForm(instance=unitm)
    return render(request, 'UnitMeasure/unitm_edit.html',
                  {'form': form})


def unit_measure_delete(request, unitm_id):
    unitm = get_object_or_404(UnitMeasure, pk=unitm_id)
    try:
        unitm.delete()
    except ProtectedError:
        messages.warning(request, _('Unit measure has related objects and can not be deleted'))
    return redirect('unitm-list')
