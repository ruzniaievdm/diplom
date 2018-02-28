from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.TypeResource.forms import TypeResourceForm
from core.TypeResource.models import TypeResource


def type_resource_list(request):
    tresources = TypeResource.objects.all().order_by('id')
    return render(request, 'TypeResource/tresource_list.html',
                  {'tresources': tresources})


def type_resource_add(request):
    if request.method == "POST":
        form = TypeResourceForm(request.POST)
        if form.is_valid():
            tresource = form.save(commit=False)
            tresource.name = form.cleaned_data['name']
            tresource.save()
            return redirect('tresource-list')
    else:
        form = TypeResourceForm()
    return render(request, 'TypeResource/tresource_add.html',
                  {'form': form})


def type_resource_edit(request, tresource_id):
    tresource = get_object_or_404(TypeResource, pk=tresource_id)
    if request.method == "POST":
        form = TypeResourceForm(request.POST, instance=tresource)
        if form.is_valid():
            tresource = form.save(commit=False)
            tresource.name = form.cleaned_data['name']
            tresource.save()
            return redirect('tresource-list')
    else:
        form = TypeResourceForm(instance=tresource)
    return render(request, 'TypeResource/tresource_edit.html',
                  {'form': form})


def type_resource_delete(request, tresource_id):
    tresource = get_object_or_404(TypeResource, pk=tresource_id)
    try:
        tresource.delete()
    except ProtectedError:
        messages.warning(request, _('Type has related objects and can not be deleted'))
    return redirect('tresource-list')
