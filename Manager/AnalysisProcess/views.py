from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.AnalysisProcess.forms import AnalysisProcessForm
from Manager.CostWorks.forms import CostWorksAnalysisFormSet
from Manager.ImportanceWorks.forms import ImportanceWorksAnalysisFormSet
from core.AnalysisProcess.models import AnalysisProcess
from core.BusinessProcessWork.models import BusinessProcessWork
from core.CostWorks.models import CostWorks
from core.ImportanceWorks.models import ImportanceWorks


def analysis_process_list(request):
    analyses_process = AnalysisProcess.objects.all().order_by('id')
    return render(request, 'AnalysisProcess/analysis_process_list.html',
                  {'analyses_process': analyses_process})

    # def make_analysis_cost(request, analysis_process_id, process_id, analysis_id):
    # CostWork.objects.create_in_bulk([(), ])
    # analysis_process = get_object_or_404(AnalysisProcess, pk=analysis_process_id)
    # analysis = get_object_or_404(Analysis, pk=analysis_id)
    # analysis_id = analysis.id
    # process = get_object_or_404(BusinessProcess, pk=process_id)
    # process_id = process.id
    # conn = psycopg2.connect("dbname=django_db user=rewalkerof")
    # cur = conn.cursor()
    # cur.execute("INSERT INTO cost_work(times_id,process_id,analysis_id) VALUE (%s,%s,%s)",
    #             (analysis_process_id, process_id, analysis_id,))
    # cur.fetclone()
    # conn.commit()
    # cur.close()
    # conn.close()
    # context = {'analysis': analysis, 'process': process, 'analysis_process': analysis_process}
    # return render(request, 'CostWork/cost_work_list.html')


def analysis_process_detail(request, analysis_process_id):
    analysis_process = get_object_or_404(AnalysisProcess, pk=analysis_process_id)
    cost_work = CostWorks.objects.all().filter(time_id=analysis_process)
    context = {'analysis_process': analysis_process, 'cost_work': cost_work}
    return render(request, 'AnalysisProcess/analysis_process_detail.html', context)


def analysis_process_make(request, analysis_process_id):
    analysis_process = get_object_or_404(AnalysisProcess, pk=analysis_process_id)
    process_id = analysis_process.process_id
    formsetCost = CostWorksAnalysisFormSet(request.POST or None)
    bpwork = BusinessProcessWork.objects.all().filter(process_id=process_id)
    cost_work = CostWorks.objects.all().filter(time_id=analysis_process)
    context = {'analysis_process': analysis_process, 'cost_work': cost_work, 'bpwork': bpwork, 'formset': formsetCost,
               'process_id': process_id}
    return render(request, 'AnalysisProcess/analysis_process_make.html', context)


def analysis_importance_works(request, analysis_process_id):
    analysis_process = get_object_or_404(AnalysisProcess, pk=analysis_process_id)
    process_id = analysis_process.process_id
    formsetImportance = ImportanceWorksAnalysisFormSet(request.POST or None)
    bpwork = BusinessProcessWork.objects.all().filter(process_id=process_id)
    importance_works = ImportanceWorks.objects.all().filter(unique=analysis_process)
    context = {'analysis_process': analysis_process, 'importance_works': importance_works, 'bpwork': bpwork,
               'formset': formsetImportance,
               'process_id': process_id}
    return render(request, 'AnalysisProcess/analysis_importance_works.html', context)


def analysis_process_add(request):
    if request.method == "POST":
        form = AnalysisProcessForm(request.POST)
        if form.is_valid():
            analysis_process = form.save(commit=False)
            analysis_process.analysis = form.cleaned_data['analysis']
            analysis_process.process = form.cleaned_data['process']
            analysis_process.save()
            return redirect('analysis_process-list')
    else:
        form = AnalysisProcessForm()
    return render(request, 'AnalysisProcess/analysis_process_add.html',
                  {'form': form})


def analysis_process_delete(request, analysis_process_id):
    analysis_process = get_object_or_404(AnalysisProcess, pk=analysis_process_id)
    try:
        analysis_process.delete()
    except ProtectedError:
        messages.warning(request, _('Аnalysis has related objects and can not be deleted'))
    return redirect('analysis_process-list')
