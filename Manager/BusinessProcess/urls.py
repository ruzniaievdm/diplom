from django.urls import include, path

from . import views

urlpatterns = [
    path('list/', views.bp_list, name='bp-list'),
    path('<int:bp_id>/', views.bp_detail, name='bp-detail'),
    path('add/', views.bp_add, name='bp-add'),
    path('<int:bp_id>/edit/', views.bp_edit, name='bp-edit'),
    path('<int:bp_id>/delete/', views.bp_delete, name='bp-delete'),
]
