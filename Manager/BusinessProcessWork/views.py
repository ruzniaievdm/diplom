from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.BusinessProcessWork.forms import BusinessProcessWorkForm
from core.BusinessProcessWork.models import BusinessProcessWork




def business_process_work_list(request):
    bpworks = BusinessProcessWork.objects.all().order_by('id')

    return render(request, 'BusinessProcessWork/bpwork_list.html',
                  {'bpworks': bpworks})


def business_process_work_add(request):
    if request.method == "POST":
        form = BusinessProcessWorkForm(request.POST, )
        if form.is_valid():
            bpwork = form.save(commit=False)
            bpwork.name = form.cleaned_data['name']
            bpwork.level = form.cleaned_data['level']
            bpwork.parent = form.cleaned_data['parent']
            bpwork.process = form.cleaned_data['process']
            bpwork.save()
            return redirect('bpwork-list')
    else:
        form = BusinessProcessWorkForm()
    return render(request, 'BusinessProcessWork/bpwork_add.html',
                  {'form': form, })


def business_process_work_edit(request, bpwork_id):
    bpwork = get_object_or_404(BusinessProcessWork, pk=bpwork_id)
    if request.method == "POST":
        form = BusinessProcessWorkForm(request.POST, instance=bpwork)
        if form.is_valid():
            bpwork = form.save(commit=False)
            bpwork.name = form.cleaned_data['name']
            bpwork.parent = form.cleaned_data['parent']
            bpwork.level = form.cleaned_data['level']
            bpwork.process = form.cleaned_data['process']
            bpwork.save(force_update=True)
            return redirect('bpwork-list')
    else:
        form = BusinessProcessWorkForm(instance=bpwork)
    return render(request, 'BusinessProcessWork/bpwork_edit.html',
                  {'form': form})


def business_process_work_delete(request, bpwork_id):
    bpwork = get_object_or_404(BusinessProcessWork, pk=bpwork_id)
    try:
        bpwork.delete()
    except ProtectedError:
        messages.error(request, ('Work has related objects and can not be deleted'))
    return redirect('bpwork-list')
