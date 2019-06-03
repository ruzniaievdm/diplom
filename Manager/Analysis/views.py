from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from Manager.Analysis.forms import AnalysisForm
from core.Analysis.models import Analysis


def analysis_list(request):
    analyses = Analysis.objects.all().order_by('id')
    return render(request, 'Analysis/analysis_list.html',
                  {'analyses': analyses})


def analysis_add(request):
    if request.method == "POST":
        form = AnalysisForm(request.POST)
        if form.is_valid():
            analysis = form.save(commit=False)
            analysis.description = form.cleaned_data['description']
            analysis.save()
            return redirect('analysis-list')
    else:
        form = AnalysisForm()
    return render(request, 'Analysis/analysis_add.html',
                  {'form': form})


def analysis_delete(request, analysis_id):
    analysis = get_object_or_404(Analysis, pk=analysis_id)
    try:
        analysis.delete()
    except ProtectedError:
        messages.warning(request, _('Аnalysis has related objects and can not be deleted'))
    return redirect('analysis-list')


