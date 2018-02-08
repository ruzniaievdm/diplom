from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.index, name='index'),
    url(r'^enterprises/$', views.EnterpriseListView.as_view(), name='enterprises'),
    url(r'enterprise/(?P<id>[0-9]+)/$', views.enterprise_detail, name='enterprise_detail'),
    url(r'business_proceses/$', views.business_proceses, name='business_proceses'),
    url(r'business_process/(?P<id>[0-9]+)/$', views.business_process_detail, name='business_process_detail')
]
