from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index,
        name='wagtaillinkchecker'),
    url(r'^scan/$', views.scan,
        name='wagtaillinkchecker_scan'),
]
