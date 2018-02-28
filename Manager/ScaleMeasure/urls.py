from django.urls import include, path

from Manager.ScaleMeasure import views

urlpatterns = [
    path('list/', views.scale_measure_list, name='mscale-list'),
    path('add/', views.scale_measure_add, name='mscale-add'),
    path('<int:mscale_id>/edit/', views.scale_measure_edit, name='mscale-edit'),
    path('<int:mscale_id>/delete/', views.scale_measure_delete, name='mscale-delete'),
]
