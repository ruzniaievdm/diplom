from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.Resource.forms import ResourceForm
from core.Resource.models import Resource


def resource_list(request):
    resources = Resource.objects.all().order_by('id')
    return render(request, 'Resource/resource_list.html',
                  {'resources': resources})


def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    return render(request, 'Resource/resource_detail.html',
                  {'resource': resource})


def resource_add(request):
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.name = form.cleaned_data['name']
            resource.cost = form.cleaned_data['cost']
            resource.type = form.cleaned_data['type']
            resource.measure = form.cleaned_data['measure']
            resource.save()
            return redirect('resource-list')
    else:
        form = ResourceForm()
    return render(request, 'Resource/resource_add.html',
                  {'form': form})


def resource_edit(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    if request.method == "POST":
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.name = form.cleaned_data['name']
            resource.cost = form.cleaned_data['cost']
            resource.type = form.cleaned_data['type']
            resource.measure = form.cleaned_data['measure']
            resource.save()
            return redirect('resource-list')
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'Resource/resource_edit.html',
                  {'form': form})


def resource_delete(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    try:
        resource.delete()
    except ProtectedError:
        messages.warning(request, _('Resource has related objects and can not be deleted'))
    return redirect('resource-list')
