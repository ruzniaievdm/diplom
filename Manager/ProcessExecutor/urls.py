from django.urls import path

from Manager.ProcessExecutor import views

urlpatterns = [
    path('list/', views.process_executor_list, name='procexec-list'),
    path('add/', views.process_executor_add, name='procexec-add'),
    path('<int:procexec_id>/detail/', views.process_executor_detail, name='procexec-detail'),
    path('<int:procexec_id>/edit/', views.process_executor_edit, name='procexec-edit'),
    path('<int:procexec_id>/delete/', views.process_executor_delete, name='procexec-delete'),
]
