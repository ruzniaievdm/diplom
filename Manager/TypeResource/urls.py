from django.urls import include, path

from Manager.TypeResource import views

urlpatterns = [
    path('list/', views.type_resource_list, name='tresource-list'),
    path('add/', views.type_resource_add, name='tresource-add'),
    path('<int:tresource_id>/edit/', views.type_resource_edit, name='tresource-edit'),
    path('<int:tresource_id>/delete/', views.type_resource_delete, name='tresource-delete'),
]
