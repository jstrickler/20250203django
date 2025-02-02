from django.contrib import admin
# Register your models here.

from superheroes.models import Superhero, Power, Enemy, City

for model in Superhero, Power, Enemy, City:
    admin.site.register(model)
