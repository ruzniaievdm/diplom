from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.ArrowWorks.forms import ArrowWorksForm
from core.ArrowWorks.models import ArrowWorks


def arrow_works_list(request):
    arrows_works = ArrowWorks.objects.all().order_by('id')
    return render(request, 'ArrowWorks/arrow_works_list.html',
                  {'arrows_works': arrows_works})


def arrow_works_add(request):
    if request.method == "POST":
        form = ArrowWorksForm(request.POST)
        if form.is_valid():
            arrow_works = form.save(commit=False)
            arrow_works.arrow = form.cleaned_data['arrow']
            arrow_works.work = form.cleaned_data['work']
            arrow_works.description = form.cleaned_data['description']
            arrow_works.save()
            return redirect('arrow_works-list')
    else:
        form = ArrowWorksForm()
    return render(request, 'ArrowWorks/arrow_works_add.html',
                  {'form': form})


def arrow_works_edit(request, arrow_works_id):
    arrow_works = get_object_or_404(ArrowWorks, pk=arrow_works_id)
    if request.method == "POST":
        form = ArrowWorksForm(request.POST, instance=arrow_works)
        if form.is_valid():
            arrow_works = form.save(commit=False)
            arrow_works.arrow = form.cleaned_data['arrow']
            arrow_works.work = form.cleaned_data['work']
            arrow_works.description = form.cleaned_data['description']
            arrow_works.save()
            return redirect('arrow_works-list')
    else:
        form = ArrowWorksForm(instance=arrow_works)
    return render(request, 'ArrowWorks/arrow_works_edit.html',
                  {'form': form})


def arrow_works_delete(request, arrow_works_id):
    arrow_works = get_object_or_404(ArrowWorks, pk=arrow_works_id)
    try:
        arrow_works.delete()
    except ProtectedError:
        messages.warning(request, _('Arrow works has related objects and can not be deleted'))
    return redirect('arrow_works-list')
