from django.contrib import admin

from superheroes.models import Superhero, Power, Enemy, City

admin.site.register(Superhero)  # register each model
admin.site.register(City)
admin.site.register(Enemy)
admin.site.register(Power)

