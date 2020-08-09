# coding: utf-8
from django.contrib import admin
from django.urls import path, include
from vdapp.client import urls as client_urls
from vdapp.dashboard import urls as dashboard_urls

urlpatterns = [
    path('dashboard/', include(dashboard_urls)),
    path('client/', include(client_urls))
]
