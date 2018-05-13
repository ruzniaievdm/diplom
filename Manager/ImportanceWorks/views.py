from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.ImportanceWorks.forms import ImportanceWorksForm
from core.ImportanceWorks.models import ImportanceWorks


def importance_works_list(request):
    importance_works = ImportanceWorks.objects.all().order_by('id')
    return render(request, 'ImportanceWorks/importance_works_list.html',
                  {'importance_works': importance_works})


def importance_works_add(request):
    if request.method == "POST":
        form = ImportanceWorksForm(request.POST)
        if form.is_valid():
            importance_work = form.save(commit=False)
            importance_work.unique = form.cleaned_data['unique']
            importance_work.work = form.cleaned_data['work']
            importance_work.elemental_importance = form.cleaned_data['elemental_importance']
            importance_work.object_importance = form.cleaned_data['object_importance']
            importance_work.relative_cost = form.cleaned_data['relative_cost']
            importance_work.relative_importance = form.cleaned_data['relative_importance']
            importance_work.save()
            return redirect('importance_works-list')
    else:
        form = ImportanceWorksForm()
    return render(request, 'ImportanceWorks/importance_works_add.html',
                  {'form': form, })


def importance_works_edit(request, importance_work_id):
    importance_work = get_object_or_404(ImportanceWorks, pk=importance_work_id)
    if request.method == "POST":
        form = ImportanceWorksForm(request.POST, instance=importance_work)
        if form.is_valid():
            importance_work = form.save(commit=False)
            importance_work.unique = form.cleaned_data['unique']
            importance_work.work = form.cleaned_data['work']
            importance_work.elemental_importance = form.cleaned_data['elemental_importance']
            importance_work.object_importance = form.cleaned_data['object_importance']
            importance_work.relative_cost = form.cleaned_data['relative_cost']
            importance_work.relative_importance = form.cleaned_data['relative_importance']
            importance_work.save()
            return redirect('importance_works-list')
    else:
        form = ImportanceWorksForm(instance=importance_work)
    return render(request, 'ImportanceWorks/importance_works_edit.html',
                  {'form': form})


def importance_works_delete(request, importance_work_id):
    importance_work = get_object_or_404(ImportanceWorks, pk=importance_work_id)
    try:
        importance_work.delete()
    except ProtectedError:
        messages.warning(request, _('Importance work has related objects and can not be deleted'))
    return redirect('importance_works-list')
