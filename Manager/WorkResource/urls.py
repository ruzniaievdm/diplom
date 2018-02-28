from django.urls import path

from Manager.WorkResource import views

urlpatterns = [
    path('list/', views.work_resource_list, name='wresource-list'),
    path('add/', views.work_resource_add, name='wresource-add'),
    path('<int:wresource_id>/edit/', views.work_resource_edit, name='wresource-edit'),
    path('<int:wresource_id>/delete/', views.work_resource_delete, name='wresource-delete'),
]
