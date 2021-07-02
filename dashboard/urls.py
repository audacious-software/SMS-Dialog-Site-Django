# pylint: disable=line-too-long

from django.conf.urls import url

from .views import dashboard_home, dashboard_dialogs, dashboard_logout, dashboard_create, \
                   dashboard_delete, dashboard_start

urlpatterns = [
    url(r'^delete$', dashboard_delete, name='dashboard_delete'),
    url(r'^create$', dashboard_create, name='dashboard_create'),
    url(r'^start$', dashboard_start, name='dashboard_start'),
    url(r'^dialogs$', dashboard_dialogs, name='dashboard_dialogs'),
    url(r'^logout$', dashboard_logout, name='dashboard_logout'),
    url(r'^$', dashboard_home, name='dashboard_home'),
]
