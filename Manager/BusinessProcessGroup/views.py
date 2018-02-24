from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.BusinessProcessGroup.forms import BusinessProcessGroupForm
from core.BusinessProcessGroup.models import BusinessProcessGroup


def bpgroup_list(request):
    bpgroups = BusinessProcessGroup.objects.all().order_by('id')

    return render(request, 'BusinessProcessGroup/bpgroup_list.html',
                  {'bpgroups': bpgroups})


def bpgroup_add(request):
    if request.method == "POST":
        form = BusinessProcessGroupForm(request.POST)
        if form.is_valid():
            bpgroup = form.save(commit=False)
            bpgroup.name = form.cleaned_data['name']
            bpgroup.save()
            return redirect('bpgroup-list')
    else:
        form = BusinessProcessGroupForm()
    return render(request, 'BusinessProcessGroup/bpgroup_add.html',
                  {'form': form})


def bpgroup_edit(request, bpgroup_id):
    bpgroup = get_object_or_404(BusinessProcessGroup, pk=bpgroup_id)
    if request.method == "POST":
        form = BusinessProcessGroupForm(request.POST, instance=bpgroup)
        if form.is_valid():
            bpgroup = form.save(commit=False)
            bpgroup.name = form.cleaned_data['name']
            bpgroup.save()
            return redirect('bpgroup-list')
    else:
        form = BusinessProcessGroupForm(instance=bpgroup)
    return render(request, 'BusinessProcessGroup/bpgroup_edit.html',
                  {'form': form})


def bpgroup_delete(request, bpgroup_id):
    bpgroup = get_object_or_404(BusinessProcessGroup, pk=bpgroup_id)

    try:
        bpgroup.delete()
    except ProtectedError:
        messages.warning(request, _('Business process group has related objects and can not be deleted'))

    return redirect('bpgroup-list')
