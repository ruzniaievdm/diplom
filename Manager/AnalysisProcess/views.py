from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from numpy import *
from Manager.AnalysisProcess.forms import AnalysisProcessForm
from Manager.CostWorks.forms import CostWorksAnalysisFormSet
from Manager.ImportanceWorks.forms import ImportanceWorksAnalysisFormSet
from core.AnalysisProcess.models import AnalysisProcess
from core.BusinessProcess.models import BusinessProcess
from core.BusinessProcessWork.models import BusinessProcessWork
from core.CostWorks.models import CostWorks
from core.ImportanceWorks.models import ImportanceWorks
from .fusioncharts import FusionCharts


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
    cost_work = CostWorks.objects.all().filter(unique_cw_id=analysis_process)
    importance_work = ImportanceWorks.objects.all().filter(unique_id=analysis_process)
    context = {'analysis_process': analysis_process, 'cost_work': cost_work, 'importance_work': importance_work}
    return render(request, 'AnalysisProcess/analysis_process_detail.html', context)


def analysis_process_make(request, analysis_process_id):
    analysis_process = get_object_or_404(AnalysisProcess, pk=analysis_process_id)
    process_id = analysis_process.process_id
    formsetCost = CostWorksAnalysisFormSet(request.POST or None)
    bpwork = BusinessProcessWork.objects.all().filter(process_id=process_id)
    cost_work = CostWorks.objects.all().filter(unique_cw_id=analysis_process)
    context = {'analysis_process': analysis_process, 'cost_work': cost_work, 'bpwork': bpwork, 'formset': formsetCost,
               'process_id': process_id}
    return render(request, 'AnalysisProcess/analysis_process_make.html', context)


def analysis_importance_works(request, analysis_process_id):
    analysis_process = get_object_or_404(AnalysisProcess, pk=analysis_process_id)
    process_id = analysis_process.process_id
    bpwork = BusinessProcessWork.objects.all().filter(process_id=process_id)
    importance_works = ImportanceWorks.objects.all().filter(unique=analysis_process)
    formsetImportance = ImportanceWorksAnalysisFormSet(request.POST or None)

    if request.method == "POST":
        print('1')
        if formsetImportance.is_valid():
            print('2')
            for form in formsetImportance:
                print('3')
                cd = form.cleaned_data
                print(cd)
                unique = analysis_process_id
                print(unique)
                work = cd.get('work')
                elemental_importance = cd.get('elemental_importance')
                object_importance = cd.get('object_importance')
                print("before")
                analysis = ImportanceWorks.objects.create(
                    unique=AnalysisProcess.objects.get(id=analysis_process_id), work=work,
                    elemental_importance=elemental_importance,
                    object_importance=object_importance)
                print(analysis.unique)
                analysis.save(force_update=True)
                messages.success(request, "lOL")


        else:
            print("ХУЙНЯ3")
            formsetImportance = ImportanceWorksAnalysisFormSet()
        return redirect('importance_works-list')
    else:
        print("ХУЙНЯ2" + request.method)

    context = {'analysis_process': analysis_process, 'importance_works': importance_works, 'bpwork': bpwork,
               'formset': formsetImportance,
               'process_id': process_id}
    return render(request, 'AnalysisProcess/analysis_importance_works.html',
                  context)  # def analysis_importance_works_add(request):


#
#     return render(request, 'AnalysisProcess/analysis_importance_works_add.html',
#                   {'formset': formsetImportance})
#

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


def analysis_process_abc(request, analysis_process_id):
    bp_work = CostWorks.objects.all().filter(unique_cw_id=analysis_process_id).order_by('-cost_work')[:5]
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Work costs",
        "paletteColors": "#0075c2",
        "bgColor": "#ffffff",
        "borderAlpha": "20",
        "usePlotGradientColor": "5",
        "plotBorderAlpha": "10",
        "xAxisLineColor": "#999999",
        "showValues": "0",
        "showTooltip": "1",
        "divlineColor": "#999999",
        "divLineIsDashed": "1",
        "theme": "fint",
        "rotateValues": "2",
        "exportEnabled": "1",
        "showHoverEffect": "1",
        "numDivLines": "3",
    }

    dataSource['data'] = []
    for key in CostWorks.objects.all():
        data = {}
        data['value'] = key.cost_work
        dataSource['data'].append(data)
        print(data)

    column2D = FusionCharts("column2D", "ex1", "600", "400", "chart-1", "json", dataSource)
    context = {'bp_work': bp_work, 'output': column2D.render()}
    return render(request, 'AnalysisProcess/analysis_process_abc.html', context)


def analysis_process_abc_second(request, analysis_process_id):
    bp_work = CostWorks.objects.all().filter(unique_cw_id=analysis_process_id).order_by('-cost_work')[:5]
    bp_work_id = CostWorks.objects.values('work_id').filter(unique_cw_id=analysis_process_id).order_by('-cost_work')[:5]
    # process = list(BusinessProcess.objects.values('name').filter(id=1))
    importance_top = list(
        ImportanceWorks.objects.values_list('elemental_importance', flat=True).filter(id__in=bp_work_id))
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Work costs",
        "paletteColors": "#0075c2",
        "bgColor": "#ffffff",
        "borderAlpha": "20",
        "canvasBorderAlpha": "0",
        "usePlotGradientColor": "5",
        "plotBorderAlpha": "10",
        "xAxisLineColor": "#999999",
        "showValues": "0",
        "divlineColor": "#999999",
        "divLineIsDashed": "1",
        "showAlternateHGridColor": "0",
        "numberPostfix": "",
    }

    dataSource['data'] = []
    for key in CostWorks.objects.all():
        data = {}
        data['value'] = key.cost_work
        data['label'] = key.id
        dataSource['data'].append(data)

    column2D = FusionCharts("column2D", "ex1", "600", "400", "chart-1", "json", dataSource)
    context = {'bp_work': bp_work, 'output': column2D.render(), 'importance_top': importance_top}
    return render(request, 'AnalysisProcess/analysis_process_abc_second.html', context)


def analysis_process_delete(request, analysis_process_id):
    analysis_process = get_object_or_404(AnalysisProcess, pk=analysis_process_id)
    try:
        analysis_process.delete()
    except ProtectedError:
        messages.warning(request, _('Аnalysis has related objects and can not be deleted'))
    return redirect('analysis_process-list')


    # analysis_process = get_object_or_404(AnalysisProcess, pk=analysis_process_id)
    # process_id = analysis_process.process_id
    # analysis_id = analysis_process.analysis_id
    # bpwork = BusinessProcessWork.objects.all().filter(process_id=process_id)
    # importance_works = ImportanceWorks.objects.all().filter(unique=analysis_process)

    # analysis_importance.unique = formsetImportance.cleaned_data['unique']
    # analysis_importance.work = formsetImportance.cleaned_data['work']
    # analysis_importance.elemental_importance = formsetImportance.cleaned_data['elemental_importance']
    # analysis_importance.object_importance = formsetImportance.cleaned_data['object_importance']
    # data = formsetImportance.cleaned_data


# def licence_medicine_add(request, licence_id):
#     request.acl.check_raise('licence', 'edit')
#     licence = get_object_or_404(Licence, pk=licence_id)
#
#     form_body = LicenceMedicineAddForm(request.POST or None,
#                                        licence=licence)
#
#     if '_cancel' in request.POST:
#         return redirect(redirect_url(request, reverse('licence-view', args=[licence.id])))
#
#     ManufacturersFormSet = formset_factory(ManufacturersForm, can_delete=True,
#                                            extra=3, formset=BaseManufacturersFormSet)
#     manufacturers_formset = ManufacturersFormSet(request.POST or None, prefix='manufacturers')
#
#     if form_body.is_valid() and manufacturers_formset.is_valid():
#         medicine = form_body.cleaned_data['code']
#         licence_item = LicenceItem()
#         licence_item.licence = licence
#         licence_item.medicine = medicine
#         licence_item.save()
#         for form in manufacturers_formset.forms:
#             manufacturer = form.save(medicine)
#             if manufacturer:
#                 licence_item.manufacturers.add(manufacturer)
#
#         log.object('licence_medicine_add',
#                    _('Manager {manager_name} added medicine {medicine_code}'
#                      ' to licence {licence_id}: {licence_licence}'),
#                    licence,
#                    medicine,
#                    request.user,
#                    manager_id=request.user.id,
#                    manager_name=request.user.label,
#                    medicine_id=medicine.id,
#                    medicine_code=medicine.code,
#                    licence_id=licence.id,
#                    licence_licence=licence.licence)
#
#         return redirect(redirect_url(request, reverse('licence-view', args=[licence.id])))
#
#     form = {'body': form_body,
#             'buttons': {'save': True, 'cancel': True}}
#
#     return render(request,
#                   'Manager/Licence/licence_medicine_add.html',
#                   {'form': form,
#                    'manufacturers_formset': manufacturers_formset,
#                    'licence': licence})

def chart(request):
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Top 10 Most Populous Countries",
        "paletteColors": "#0075c2",
        "bgColor": "#ffffff",
        "borderAlpha": "20",
        "canvasBorderAlpha": "0",
        "usePlotGradientColor": "0",
        "plotBorderAlpha": "10",
        "showXAxisLine": "1",
        "xAxisLineColor": "#999999",
        "showValues": "0",
        "divlineColor": "#999999",
        "divLineIsDashed": "1",
        "showAlternateHGridColor": "0"
    }

    dataSource['data'] = []
    for key in CostWorks.objects.all():
        data = {}
        data['label'] = key.cost_work
        data['value'] = key.cost_work
        dataSource['data'].append(data)

    column2D = FusionCharts("column2D", "ex1", "600", "400", "chart-1", "json", dataSource)
    return render(request, 'AnalysisProcess/analysis_process_abc.html', {'output': column2D.render()})
