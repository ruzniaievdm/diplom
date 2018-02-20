from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('enterprises/', views.EnterpriseListView.as_view(), name='enterprises'),
    path('enterprise/<int:id>/', views.enterprise_detail, name='enterprise_detail'),
    path('enterprise/new/', views.enterprise_new, name='enterprise_new'),
    path('enterprise/<int:id>/edit/', views.enterprise_edit, name='enterprise_edit'),
    path('business_proceses/', views.business_proceses, name='business_proceses'),
    path('business_process/<int:id>/', views.business_process_detail, name='business_process_detail'),
    path('analysis/', views.analysis_list, name='analysis_list'),
]
