from django.urls import include, path

from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('business_proceses/', views.business_proceses, name='business_proceses'),
    path('business_process/<int:id>/', views.business_process_detail, name='business_process_detail'),
    path('analysis/', views.analysis_list, name='analysis_list'),
]
