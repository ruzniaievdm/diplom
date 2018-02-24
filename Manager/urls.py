from django.urls import include, path

urlpatterns = [
    path('enterprise/', include('Manager.Enterprise.urls'), name='enterprise'),
    path('bpgroup/', include('Manager.BusinessProcessGroup.urls'), name='bpgroup'),
    path('bp/', include('Manager.BusinessProcess.urls'), name='bp'),
    path('department/', include('Manager.Department.urls'), name='department'),
    path('position/', include('Manager.PositionEmployee.urls'), name='position'),
    path('employee/', include('Manager.Employee.urls'), name='employee'),
]
