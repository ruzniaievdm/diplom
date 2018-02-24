from django.urls import include, path

from . import views

urlpatterns = [
    path('list/', views.bpgroup_list, name='bpgroup-list'),
    path('add/', views.bpgroup_add, name='bpgroup-add'),
    path('<int:bpgroup_id>/edit/', views.bpgroup_edit, name='bpgroup-edit'),
    path('<int:bpgroup_id>/delete/', views.bpgroup_delete, name='bpgroup-delete'),
]