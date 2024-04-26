"""sms_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import sys

if sys.version_info[0] > 2:
    from django.urls import re_path as url, include # pylint: disable=no-name-in-module
else:
    from django.conf.urls import url, include

from django.contrib import admin
from django.urls import path

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^builder/', include('django_dialog_engine_builder.urls')),
    url(r'^messages/', include('simple_messaging.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^quicksilver/', include('quicksilver.urls')),
    url(r'^generative-ai/', include('simple_generative_ai.urls')),
]
