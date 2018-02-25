from django.urls import include, path

from Manager import views

urlpatterns = [
    path('manager/', views.index, name='index'),
    path('enterprise/', include('Manager.Enterprise.urls'), name='enterprise'),
    path('bpgroup/', include('Manager.BusinessProcessGroup.urls'), name='bpgroup'),
    path('bp/', include('Manager.BusinessProcess.urls'), name='bp'),
    path('department/', include('Manager.Department.urls'), name='department'),
    path('position/', include('Manager.PositionEmployee.urls'), name='position'),
    path('employee/', include('Manager.Employee.urls'), name='employee'),
    path('procexec/', include('Manager.ProcessExecutor.urls'), name='procexec'),
    path('arrowtype/', include('Manager.ArrowType.urls'), name='atype'),
    path('arrowgloss/', include('Manager.GlossaryArrow.urls'), name='arrowgloss'),
    path('bpwork/', include('Manager.BusinessProcessWork.urls'), name='bpwork'),
    path('tresource/', include('Manager.TypeResource.urls'), name='tresource'),
    path('mscale/', include('Manager.ScaleMeasure.urls'), name='mscale'),
    path('unitm/', include('Manager.UnitMeasure.urls'), name='unitm'),
    path('resource/', include('Manager.Resource.urls'), name='resource'),
]
