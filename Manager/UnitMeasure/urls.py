from django.urls import path

from Manager.UnitMeasure import views

urlpatterns = [
    path('list/', views.unit_measure_list, name='unitm-list'),
    path('add/', views.unit_measure_add, name='unitm-add'),
    path('<int:unitm_id>/edit/', views.unit_measure_edit, name='unitm-edit'),
    path('<int:unitm_id>/delete/', views.unit_measure_delete, name='unitm-delete'),
]
