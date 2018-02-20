from django.urls import include, path

from . import views

urlpatterns = [
    path('list/', views.enterprise_list, name='enterprise-list'),
    path('<int:enterprise_id>/', views.enterprise_detail, name='enterprise-detail'),
    path('new/', views.enterprise_add, name='enterprise-add'),
    path('<int:enterprise_id>/edit/', views.enterprise_edit, name='enterprise-edit'),
    path('<int:enterprise_id>/delete/', views.enterprise_delete, name='enterprise-delete'),
]
