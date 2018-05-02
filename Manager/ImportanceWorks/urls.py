from django.urls import path

from Manager.ImportanceWorks import views

urlpatterns = [
    path('list/', views.importance_works_list, name='importance_works-list'),
    path('add/', views.importance_works_add, name='importance_works-add'),
    path('<int:importance_work_id>/edit/', views.importance_works_edit, name='importance_works-edit'),
    path('<int:importance_work_id>/delete/', views.importance_works_delete, name='importance_works-delete'),
]
