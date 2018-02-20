from django.urls import include, path


urlpatterns = [
    path('enterprise/', include('Manager.Enterprise.urls'), name='enterprise'),
]
