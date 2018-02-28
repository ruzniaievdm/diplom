from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.ProcessExecutor.forms import ProcessExecutorForm
from core.ProcessExecutor.models import ProcessExecutor


def process_executor_list(request):
    procexecs = ProcessExecutor.objects.all().order_by('id')
    return render(request, 'ProcessExecutor/procexec_list.html', {'procexecs': procexecs})


def process_executor_detail(request, procexec_id):
    procexec = get_object_or_404(ProcessExecutor, pk=procexec_id)
    return render(request, 'ProcessExecutor/procexec_detail.html', {'procexec': procexec})


def process_executor_add(request):
    if request.method == "POST":
        form = ProcessExecutorForm(request.POST)
        if form.is_valid():
            procexec = form.save(commit=False)
            procexec.department = form.cleaned_data['department']
            procexec.business_process = form.cleaned_data['business_process']
            procexec.employee = form.cleaned_data['employee']
            procexec.save()
            return redirect('procexec-list')
    else:
        form = ProcessExecutorForm()
    return render(request, 'ProcessExecutor/procexec_add.html',
                  {'form': form})


def process_executor_edit(request, procexec_id):
    procexec = get_object_or_404(ProcessExecutor, pk=procexec_id)
    if request.method == "POST":
        form = ProcessExecutorForm(request.POST, instance=procexec)
        if form.is_valid():
            procexec = form.save(commit=False)
            procexec.department = form.cleaned_data['department']
            procexec.business_process = form.cleaned_data['business_process']
            procexec.employee = form.cleaned_data['employee']
            procexec.save()
            return redirect('procexec-list')
    else:
        form = ProcessExecutorForm(instance=procexec)
    return render(request, 'ProcessExecutor/procexec_edit.html',
                  {'form': form})


# def process_executor_edit(request, procexec_id):
#     procexec = get_object_or_404(ProcessExecutor, pk=procexec_id)
#     if request.method == "POST":
#         form = ProcessExecutorForm(request.POST, instance=procexec)
#         if form.is_valid():
#             procexec = form.save(commit=False)
#             procexec.department = form.cleaned_data['department']
#             procexec.business_process = form.cleaned_data['business_process']
#             procexec.employee = form.cleaned_data['employee']
#             procexec.save()
#             return redirect('procexec-list')
#     else:
#         form = ProcessExecutor(instance=procexec)
#     return render(request, 'ProcessExecutor/procexec_edit.html', {'form': form})



def process_executor_delete(request, procexec_id):
    procexec = get_object_or_404(ProcessExecutor, pk=procexec_id)
    try:
        procexec.delete()
    except ProtectedError:
        messages.warning(request, _('Process Executor has related objects and can not be deleted'))
    return redirect('procexec-list')