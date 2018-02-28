from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.WorkResource.forms import WorkResourceForm
from core.WorkResource.models import WorkResource


def work_resource_list(request):
    wresources = WorkResource.objects.all().order_by('id')
    return render(request, 'WorkResource/wresource_list.html', {'wresources': wresources})


def work_resource_add(request):
    if request.method == "POST":
        form = WorkResourceForm(request.POST)
        if form.is_valid():
            wresource = form.save(commit=False)
            wresource.work = form.cleaned_data['work']
            wresource.resource = form.cleaned_data['resource']
            wresource.expense = form.cleaned_data['expense']
            wresource.save()
            return redirect('wresource-list')
    else:
        form = WorkResourceForm()
    return render(request, 'WorkResource/wresource_add.html',
                  {'form': form})


def work_resource_edit(request, wresource_id):
    wresource = get_object_or_404(WorkResource, pk=wresource_id)
    if request.method == "POST":
        form = WorkResourceForm(request.POST, instance=wresource)
        if form.is_valid():
            wresource = form.save(commit=False)
            wresource.work = form.cleaned_data['work']
            wresource.resource = form.cleaned_data['resource']
            wresource.expense = form.cleaned_data['expense']
            wresource.save()
            return redirect('wresource-list')
    else:
        form = WorkResourceForm(instance=wresource)
    return render(request, 'WorkResource/wresource_edit.html',
                  {'form': form})


def work_resource_delete(request, wresource_id):
    wresource = get_object_or_404(WorkResource, pk=wresource_id)
    try:
        wresource.delete()
    except ProtectedError:
        messages.warning(request, _('Work resource has related objects and can not be deleted'))
    return redirect('wresource-list')
