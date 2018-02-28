from django.urls import include, path

from Manager.ArrowType import views

urlpatterns = [
    path('list/', views.arrow_type_list, name='atype-list'),
    path('add/', views.arrow_type_add, name='atype-add'),
    path('<int:atype_id>/edit/', views.arrow_type_edit, name='atype-edit'),
    path('<int:atype_id>/delete/', views.arrow_type_delete, name='atype-delete'),
]
