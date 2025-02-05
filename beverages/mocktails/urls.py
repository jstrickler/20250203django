from django.urls import path
from . import views

app_name = "mocktails"

urlpatterns = [
    path("", views.home, name="home"),
    path("drinklist", views.drinklist, name="drinklist")
]
