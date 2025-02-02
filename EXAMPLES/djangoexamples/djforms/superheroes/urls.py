"""
URL Configuration for djforms/superheroes
"""
from django.urls import path
from . import views

app_name = 'djforms'

urlpatterns = [
    path('', views.home, name='home'),
    path('demo', views.demo, name='demo'),
    path('heroadd/<str:layout_type>', views.heroadd, name='heroadd'),
    path('herodelete', views.herodelete, name='herodelete'),
    path('herodeletedropdown', views.herodeletedropdown, name='herodeletedropdown'),
    path('herolist', views.herolist, name='herolist'),
    path('herodetails/<str:hero_name>', views.herodetails, name='herodetails'),
    path('heroadded/<str:hero_name>', views.heroadded, name='heroadded'),
] 

