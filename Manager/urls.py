from django.urls import include, path
from Manager import views

urlpatterns = [
    path('', views.index, name='index'),
    path('atype/', include('Manager.ArrowType.urls'), name='atype'),
    path('bp/', include('Manager.BusinessProcess.urls'), name='bp'),
    path('bpgroup/', include('Manager.BusinessProcessGroup.urls'), name='bpgroup'),
    path('bpwork/', include('Manager.BusinessProcessWork.urls'), name='bpwork'),
    path('department/', include('Manager.Department.urls'), name='department'),
    path('employee/', include('Manager.Employee.urls'), name='employee'),
    path('enterprise/', include('Manager.Enterprise.urls'), name='enterprise'),
    path('arrowgloss/', include('Manager.GlossaryArrow.urls'), name='arrowgloss'),
    path('position/', include('Manager.PositionEmployee.urls'), name='position'),
    path('procexec/', include('Manager.ProcessExecutor.urls'), name='procexec'),
    path('resource/', include('Manager.Resource.urls'), name='resource'),
    path('mscale/', include('Manager.ScaleMeasure.urls'), name='mscale'),
    path('tresource', include('Manager.TypeResource.urls'), name='tresource'),
    path('unitm/', include('Manager.UnitMeasure.urls'), name='unitm'),
    path('wresource/', include('Manager.WorkResource.urls'), name='wresource'),
    path('analysis/', include('Manager.Analysis.urls'), name='analysis'),
    path('cost_works/', include('Manager.CostWorks.urls'), name='cost_works'),
    path('analysis_process/', include('Manager.AnalysisProcess.urls'), name='analysis_process'),
    path('importance_works/', include('Manager.ImportanceWorks.urls'), name='importance_works'),
    path('arrow_works/', include('Manager.ArrowWorks.urls'), name='arrows_works'),
    path('recommendations/', include('Manager.Recommendations.urls'), name='recommendations'),
    path('report/', include('Manager.Report.urls'), name='report'),

]
