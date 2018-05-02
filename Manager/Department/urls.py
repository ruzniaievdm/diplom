from django.urls import include, path

from . import views

urlpatterns = [
    path('list/', views.department_list, name='department-list'),
    path('add/', views.department_add, name='department-add'),
    path('<int:department_id>/edit/', views.department_edit, name='department-edit'),
    path('<int:department_id>/delete/', views.department_delete, name='department-delete'),
]
