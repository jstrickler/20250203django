from django.contrib import admin
# Register your models here.

from .models import Superhero, Power, City, Enemy

for model in Superhero, Power, City, Enemy:
    admin.site.register(model)
