# -*- coding: utf-8 -*-
import json

from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _
import codecs
from Manager.Report.forms import ReportForm
from Manager.Report.fusioncharts import FusionCharts
from core.Recommendations.models import Recommendations
from core.Report.models import Report


def report_list(request):
    reports = Report.objects.all().order_by('id')
    return render(request, 'Report/report_list.html',
                  {'reports': reports})


def report_add(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            analysis = form.save(commit=False)
            analysis.description = form.cleaned_data['description']
            analysis.save()
            return redirect('report-list')
    else:
        form = ReportForm()
    return render(request, 'Report/report_add.html',
                  {'form': form})


def report_detail(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    recommendations = Recommendations.objects.all().filter(report_id=report_id)
    return render(request, 'Report/report_detail.html',
                  {'report': report, 'recommendations': recommendations})


def report_chart(request, report_id):
    dataSource = {}
    recommendations = Recommendations.objects.all().filter(report_id=report_id)
    dataSource['chart'] = {
        "caption": "Before analysis",
        "bgColor": "#ffffff",
        "borderAlpha": "20",
        "usePlotGradientColor": "5",
        "plotBorderAlpha": "10",
        "xAxisName": "Works",
        "showValues": "1",
        "showLabels": "2",
        "divlineColor": "#999999",
        "divLineIsDashed": "1",
        "exportEnabled": "1",
        "numDivLines": "3",
        "use3DLighting": "0",
        "showaxislines": "1",
        "theme": "hulk-light",
    }

    dataSource["categories"] = [{
        "category": [
            {"label": "2"},
            {"label": "8"},
            {"label": "10"},
            {"label": "12"},
            {"label": "4"}
        ]
    }]
    dataSource["dataset"] = [{
        "seriesname": "Relative importance",
        "data": [
            {"value": "0.239"},
            {"value": "0.191"},
            {"value": "0.152"},
            {"value": "0.122"},
            {"value": "0.295"}
        ]
    }, {
        "seriesname": "Relative cost",
        "data": [
            {"value": "0.142"},
            {"value": "0.233"},
            {"value": "0.162"},
            {"value": "0.084"},
            {"value": "0.379"}
        ]
    }
    ]
    # dataSource['data'] = []

    # print(recommendations)
    # for key in recommendations:
    #     data = {}
    #     data['value'] = key.relative_cost
    #     data['label'] = json.dumps(key.work.id, ensure_ascii=False)
    #     dataSource['data'].append(data)
    # print(type(key.work.name))
    # print(data)

    mscol2D = FusionCharts("mscolumn2D", "ex1", "450", "400", "chart-1", "json", dataSource)
    mscol2D2 = FusionCharts("mscolumn2D", "ex2", "450", "400", "chart-2", "json", dataSource)
    context = {'recommendations': recommendations, 'output': mscol2D.render(), 'output2': mscol2D2.render(), }
    return render(request, 'Report/report_chart.html', context)


def report_delete(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    try:
        report.delete()
    except ProtectedError:
        messages.warning(request, _('Report for recommendations has related objects and can not be deleted'))
    return redirect('report-list')
