from django.urls import path

from Manager.Profile import views

urlpatterns = [
    path('profiles', views.ProfileFamilyMemberCreate.as_view(), name='profiles')
]
