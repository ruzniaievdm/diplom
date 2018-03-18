from django.urls import include, path

from Manager.Analysis import views

urlpatterns = [
    path('list/', views.analysis_list, name='analysis-list'),
    path('add/', views.analysis_add, name='analysis-add'),
    path('<int:analysis_id>/delete/', views.analysis_delete, name='analysis-delete'),
]
