from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from Manager.AnalysisProcess.forms import AnalysisProcessForm
from Manager.CostWorks.forms import CostWorksAnalysisForm
from core.BusinessProcessWork.models import BusinessProcessWork

from core.CostWorks.models import CostWorks


def cost_works_list(request):
    cost_works = CostWorks.objects.all().order_by('id')
    # print(cost_works)
    # bps = BusinessProcess.objects.all().order_by('id')
    return render(request, 'CostWorks/cost_works_list.html',
                  {'cost_works': cost_works})


# def cost_works_detail(request, analysis_process_id):
#     cost_work = get_object_or_404(CostWorks, time=analysis_process_id)
#     return render(request, 'CostWorks/cost_works_detail.html',
#                   {'cost_work': cost_work})


def cost_works_add(request):
    if request.method == "POST":
        form = CostWorksAnalysisForm(request.POST)
        if form.is_valid():
            cw = form.save(commit=False)
            cw.unique_cw = form.cleaned_data['unique_cw']
            cw.work = form.cleaned_data['work']
            cw.kind = form.cleaned_data['kind']
            cw.cost_work = form.cleaned_data['cost_work']
            cw.duration = form.cleaned_data['duration']
            cw.save()
            return redirect('cost_works-list')
    else:
        form = CostWorksAnalysisForm()

    return render(request, 'CostWorks/cost_works_add.html',
                  {'form': form, })


def cost_works_edit(request, cost_work_id):
    cost_work = get_object_or_404(CostWorks, pk=cost_work_id)
    if request.method == "POST":
        form = CostWorksAnalysisForm(request.POST, instance=cost_work)
        if form.is_valid():
            cost_work = form.save(commit=False)
            cost_work.work = form.cleaned_data['work']
            cost_work.kind = form.cleaned_data['kind']
            cost_work.cost_work = form.cleaned_data['cost_work']
            cost_work.unique_cw = form.cleaned_data['unique_cw']
            cost_work.duration = form.cleaned_data['duration']
            cost_work.save()
            return redirect('cost_works-list')
    else:
        form = CostWorksAnalysisForm(instance=cost_work)
    return render(request, 'CostWorks/cost_works_edit.html',
                  {'form': form})



    # process_id =1,4
    # bp = get_object_or_404(BusinessProcess, pk=process_id)
    # bpwork = BusinessProcessWork.objects.filter(process_id=1)  # process_id
    # formset = CostWorksAnalysisFormSet(request.POST or None)
    # context = {'cost_work': cost_work, 'formset': formset, 'bpwork': bpwork, }
    # return render(request, 'CostWorks/cost_works_edit.html', context)


def cost_works_delete(request, cost_work_id):
    cost_work = get_object_or_404(CostWorks, pk=cost_work_id)
    try:
        cost_work.delete()
    except ProtectedError:
        messages.warning(request, _('Analysis cost has related objects and can not be deleted'))
    return redirect('cost_works-list')
