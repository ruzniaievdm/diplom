from django.urls import path

from Manager.Resource import views

urlpatterns = [
    path('list/', views.resource_list, name='resource-list'),
    path('<int:resource_id>/', views.resource_detail, name='resource-detail'),
    path('add/', views.resource_add, name='resource-add'),
    path('<int:resource_id>/edit/', views.resource_edit, name='resource-edit'),
    path('<int:resource_id>/delete/', views.resource_delete, name='resource-delete'),
]
