from django.urls import include, path

from . import views

urlpatterns = [
    path('list/', views.employee_list, name='employee-list'),
    path('add/', views.employee_add, name='employee-add'),
    path('<int:employee_id>/edit/', views.employee_edit, name='employee-edit'),
    path('<int:employee_id>/delete', views.employee_delete, name='employee-delete'),
    path('<int:employee_id>/detail', views.employee_detail, name='employee-detail'),
]
