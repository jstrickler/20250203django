from django.contrib import admin
# Register your models here.

from superheroes.models import Superhero, Power, Enemy, City # import your models

admin.site.register(Superhero)  # register each model
admin.site.register(City) # register each model
admin.site.register(Enemy) # register each model
admin.site.register(Power) # register each model
