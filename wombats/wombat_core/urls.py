"""
URL Configuration for wombat_core
"""
from django.urls import path
from . import views   # import views from app

app_name = "wombat_core"

urlpatterns = [
    # add url patterns for the wombat_core app here

    # Examples:
    path('', views.home, name='home'),
    # path('spam' ...)
    # path('thing', views.thing, name='thing'),
]
