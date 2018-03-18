# coding=utf-8
from django.conf.urls import url

from rest_framework import routers
from rest_framework.authtoken import views

from Api.BusinessProcessWork.views import BusinessProcessWorkViewSet

router = routers.DefaultRouter()
router.register(r'api-bp-work', BusinessProcessWorkViewSet, base_name='api-bp-work')

urlpatterns = router.urls

urlpatterns += [
    url(r'^auth/', views.obtain_auth_token),
]
