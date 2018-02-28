from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.ScaleMeasure.forms import ScaleMeasureForm
from core.ScaleMeasure.models import ScaleMeasure


def scale_measure_list(request):
    mscales = ScaleMeasure.objects.all().order_by('id')
    return render(request, 'ScaleMeasure/mscale_list.html',
                  {'mscales': mscales})


def scale_measure_add(request):
    if request.method == "POST":
        form = ScaleMeasureForm(request.POST)
        if form.is_valid():
            mscale = form.save(commit=False)
            mscale.name = form.cleaned_data['name']
            mscale.save()
            return redirect('mscale-list')
    else:
        form = ScaleMeasureForm()
    return render(request, "ScaleMeasure/mscale_add.html",
                  {'form': form})


def scale_measure_edit(request, mscale_id):
    mscale = get_object_or_404(ScaleMeasure, pk=mscale_id)
    if request.method == "POST":
        form = ScaleMeasureForm(request.POST, instance=mscale)
        if form.is_valid():
            mscale = form.save(commit=False)
            mscale.name = form.cleaned_data['name']
            mscale.save()
            return redirect('mscale-list')
    else:
        form = ScaleMeasureForm(instance=mscale)
    return render(request, 'ScaleMeasure/mscale_edit.html',
                  {'form': form})


def scale_measure_delete(request, mscale_id):
    mscale = get_object_or_404(ScaleMeasure, pk=mscale_id)
    try:
        mscale.delete()
    except ProtectedError:
        messages.warning(request, _('Scale has related objects and can not be deleted'))
    return redirect('mscale-list')
