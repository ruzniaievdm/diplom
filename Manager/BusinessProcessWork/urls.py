from django.urls import include, path

from Manager.BusinessProcessWork import views

urlpatterns = [
    path('list/', views.business_process_work_list, name='bpwork-list'),
    path('add/', views.business_process_work_add, name='bpwork-add'),
    path('<int:bpwork_id>/edit/', views.business_process_work_edit, name='bpwork-edit'),
    path('<int:bpwork_id>/delete/', views.business_process_work_delete, name='bpwork-delete'),

]
