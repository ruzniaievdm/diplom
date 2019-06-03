from django.urls import path

from Manager.ArrowWorks import views

urlpatterns = [
    path('list/', views.arrow_works_list, name='arrow_works-list'),
    path('add/', views.arrow_works_add, name='arrow_works-add'),
    path('<int:arrow_works_id>/edit/', views.arrow_works_edit, name='arrow_works-edit'),
    path('<int:arrow_works_id>/delete/', views.arrow_works_delete, name='arrow_works-delete'),
]
