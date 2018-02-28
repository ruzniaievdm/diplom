from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.ArrowType.forms import ArrowTypeForm
from core.ArrowType.models import ArrowType


def arrow_type_list(request):
    atypes = ArrowType.objects.all().order_by('id')
    return render(request, 'ArrowType/atype_list.html',
                  {'atypes': atypes})


def arrow_type_add(request):
    if request.method == "POST":
        form = ArrowTypeForm(request.POST)
        if form.is_valid():
            atype = form.save(commit=False)
            atype.name = form.cleaned_data['name']
            atype.short_name = form.cleaned_data['short_name']
            atype.save()
            return redirect('atype-list')
    else:
        form = ArrowTypeForm()
    return render(request, 'ArrowType/atype_add.html',
                  {'form': form})


def arrow_type_edit(request, atype_id):
    atype = get_object_or_404(ArrowType, pk=atype_id)
    if request.method == "POST":
        form = ArrowTypeForm(request.POST, instance=atype)
        if form.is_valid():
            atype = form.save(commit=False)
            atype.name = form.cleaned_data['name']
            atype.short_name = form.cleaned_data['short_name']
            atype.save()
            return redirect('atype-list')
    else:
        form = ArrowTypeForm(instance=atype)
    return render(request, 'ArrowType/atype_edit.html',
                  {'form': form})


def arrow_type_delete(request, atype_id):
    atype = get_object_or_404(ArrowType, pk=atype_id)
    try:
        atype.delete()
    except ProtectedError:
        messages.warning(request, _('Arrow type has related objects and can not be deleted'))

    return redirect('atype-list')
