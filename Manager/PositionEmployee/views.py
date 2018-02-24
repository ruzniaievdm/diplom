from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.PositionEmployee.forms import PositionEmployeeForm
from core.PositionEmployee.models import PositionEmployee


def position_list(request):
    positions = PositionEmployee.objects.all().order_by('id')
    return render(request, 'PositionEmployee/position_list.html',
                  {'positions': positions})



def position_add(request):
    if request.method == "POST":
        form = PositionEmployeeForm(request.POST)
        if form.is_valid():
            position = form.save(commit=False)
            position.name = form.cleaned_data['name']
            position.save()
            return redirect('position-list')
    else:
        form = PositionEmployeeForm()
    return render(request, 'PositionEmployee/position_add.html',
                  {'form': form})


def position_edit(request, position_id):
    position = get_object_or_404(PositionEmployee, pk=position_id)
    if request.method == "POST":
        form = PositionEmployeeForm(request.POST, instance=position)
        if form.is_valid():
            position = form.save(commit=False)
            position.name = form.cleaned_data['name']
            position.save()
            return redirect('position-list')
    else:
        form = PositionEmployeeForm(instance=position)
    return render(request, 'PositionEmployee/position_edit.html',
                  {'form': form})


def position_delete(request, position_id):
    position = get_object_or_404(PositionEmployee, pk=position_id)
    try:
        position.delete()
    except ProtectedError:
        messages.warning(request, _('Position Employee has related objects and can not be deleted'))
    return redirect('position-list')
