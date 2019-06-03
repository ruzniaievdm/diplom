from django.urls import include, path

from Manager.Report import views

urlpatterns = [
    path('list/', views.report_list, name='report-list'),
    path('add/', views.report_add, name='report-add'),
    path('<int:report_id>/delete/', views.report_delete, name='report-delete'),
    path('<int:report_id>/detail/', views.report_detail, name='report-detail'),
    path('<int:report_id>/chart/', views.report_chart, name='report-chart'),

]
