from django.shortcuts import render

from core.Analysis.models import Analysis
from core.AnalysisProcess.models import AnalysisProcess
from core.ArrowWorks.models import ArrowWorks
from core.BusinessProcessWork.models import BusinessProcessWork

from core.CostWorks.models import CostWorks
from core.GlossaryArrow.models import GlossaryArrow
from core.ArrowType.models import ArrowType
from core.BusinessProcess.models import BusinessProcess
from core.BusinessProcessGroup.models import BusinessProcessGroup
from core.Department.models import Department
from core.Employee.models import Employee
from core.Enterprise.models import Enterprise
from core.ImportanceWorks.models import ImportanceWorks
from core.PositionEmployee.models import PositionEmployee
from core.ProcessExecutor.models import ProcessExecutor
from core.Recommendations.models import Recommendations
from core.Report.models import Report
from core.Resource.models import Resource
from core.TypeResource.models import TypeResource
from core.UnitMeasure.models import UnitMeasure
from core.WorkResource.models import WorkResource


def index(request):
    num_enterprise = Enterprise.objects.all().count()
    num_bp = BusinessProcess.objects.all().count()
    num_bpgroup = BusinessProcessGroup.objects.all().count()
    num_department = Department.objects.all().count()
    num_position = PositionEmployee.objects.all().count()
    num_employee = Employee.objects.all().count()
    num_procexec = ProcessExecutor.objects.all().count()
    num_atype = ArrowType.objects.all().count()
    num_arrowgloss = GlossaryArrow.objects.all().count()
    num_bpwork = BusinessProcessWork.objects.all().count()
    num_tresource = TypeResource.objects.all().count()
    num_unitm = UnitMeasure.objects.all().count()
    num_resource = Resource.objects.all().count()
    num_wresource = WorkResource.objects.all().count()
    num_analysis = Analysis.objects.all().count()
    num_cost_works = CostWorks.objects.all().count()
    num_importance_works = ImportanceWorks.objects.all().count()
    num_analysis_process = AnalysisProcess.objects.all().count()
    num_arrow_works = ArrowWorks.objects.all().count()
    num_recommedations = Recommendations.objects.all().count()
    num_report = Report.objects.all().count()
    return render(request, 'index.html',
                  context={'num_enterprise': num_enterprise, 'num_bp': num_bp, 'num_bpgroup': num_bpgroup,
                           'num_department': num_department, 'num_position': num_position,
                           'num_employee': num_employee, 'num_procexec': num_procexec, 'num_atype': num_atype,
                           'num_arrowgloss': num_arrowgloss, 'num_bpwork': num_bpwork, 'num_tresource': num_tresource,
                           'num_unitm': num_unitm, 'num_resource': num_resource, 'num_wresource': num_wresource,
                           'num_analysis': num_analysis, 'num_cost_works': num_cost_works,
                           'num_analysis_process': num_analysis_process,
                           'num_importance_works': num_importance_works, 'num_arrow_works': num_arrow_works,
                           'num_recommendations': num_recommedations, 'num_report': num_report})
