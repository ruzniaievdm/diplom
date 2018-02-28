from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.GlossaryArrow.forms import GlossaryArrowForm
from core.GlossaryArrow.models import GlossaryArrow


def glossary_arrow_list(request):
    arrowglosses = GlossaryArrow.objects.all().order_by('id')
    return render(request, 'GlossaryArrow/arrowgloss_list.html',
                  {'arrowglosses': arrowglosses})


def glossary_arrow_add(request):
    if request.method == "POST":
        form = GlossaryArrowForm(request.POST)
        if form.is_valid():
            arrowgloss = form.save(commit=False)
            arrowgloss.arrow_description = form.cleaned_data['arrow_description']
            arrowgloss.type = form.cleaned_data['type']
            arrowgloss.save()
            return redirect('arrowgloss-list')
    else:
        form = GlossaryArrowForm()
    return render(request, 'GlossaryArrow/arrowgloss_add.html',
                  {'form': form})


def glossary_arrow_edit(request, arrowgloss_id):
    arrowgloss = get_object_or_404(GlossaryArrow, pk=arrowgloss_id)
    if request.method == "POST":
        form = GlossaryArrowForm(request.POST, instance=arrowgloss)
        if form.is_valid():
            arrowgloss = form.save(commit=False)
            arrowgloss.arrow_description = form.cleaned_data['arrow_description']
            arrowgloss.type = form.cleaned_data['type']
            arrowgloss.save()
            return redirect('arrowgloss-list')
    else:
        form = GlossaryArrowForm(instance=arrowgloss)
    return render(request, 'GlossaryArrow/arrowgloss_edit.html',
                  {'form': form})


def glossary_arrow_delete(request, arrowgloss_id):
    arrowgloss = get_object_or_404(GlossaryArrow, pk=arrowgloss_id)
    try:
        arrowgloss.delete()
    except ProtectedError:
        messages.warning(request, _('Arrow has related objects and can not be deleted'))
    return redirect('arrowgloss-list')
