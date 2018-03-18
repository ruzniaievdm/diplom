from django.urls import path

from Manager.CostWork import views

urlpatterns = [
    path('list/', views.cost_work_list, name='cost_work-list'),
    path('<int:cost_work_id>/detail/', views.cost_work_detail, name='cost_work-detail'),
    path('add/', views.cost_work_add, name='cost_work-add'),
    path('<int:cost_work_id>/edit/', views.cost_work_edit, name='cost_work-edit'),
    path('<int:cost_work_id>/delete/', views.cost_work_delete, name='cost_work-delete'),
]
