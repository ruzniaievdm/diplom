from django.urls import include, path

from . import views

urlpatterns = [
    path('list/', views.position_list, name='position-list'),
    path('add/', views.position_add, name='position-add'),
    path('<int:position_id>/edit/', views.position_edit, name='position-edit'),
    path('<int:position_id>/delete/', views.position_delete, name='position-delete'),
]
