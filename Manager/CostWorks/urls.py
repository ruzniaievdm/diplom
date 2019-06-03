from django.urls import path

from Manager.CostWorks import views

urlpatterns = [
    path('list/', views.cost_works_list, name='cost_works-list'),
    path('add/', views.cost_works_add, name='cost_works-add'),
    path('<int:cost_work_id>/edit/', views.cost_works_edit, name='cost_works-edit'),
    # path('<int:analysis_process_id>/detail/', views.cost_works_detail, name='cost_works-detail'),
    path('<int:cost_work_id>/delete/', views.cost_works_delete, name='cost_works-delete'),
]
