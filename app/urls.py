from django.urls import path

from Manager import views

urlpatterns = [
    path('manager/', views.index, name='index'),
]
