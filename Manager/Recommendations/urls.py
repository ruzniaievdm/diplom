from django.urls import path

from Manager.Recommendations import views

urlpatterns = [
    path('list/', views.recommendations_list, name='recommendations-list'),
    path('add/', views.recommendations_add, name='recommendations-add'),
    path('<int:recommendations>/delete/', views.recommendations_delete, name='recommendations-delete'),
]
