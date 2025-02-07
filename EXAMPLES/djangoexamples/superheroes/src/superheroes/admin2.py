from django.contrib import admin
from superheroes.models import Superhero, Power, Enemy, City # import your models

class SuperheroPowersInline(admin.TabularInline):
    model = Superhero.powers.through

class EnemyPowersInline(admin.TabularInline):
    model = Enemy.powers.through

# customize the admin for this model
class PowerAdmin(admin.ModelAdmin):  # create custom Admin model
    search_fields = ['name', 'description'] # add Admin metadata
    inlines = [SuperheroPowersInline, EnemyPowersInline]

class SuperHeroAdmin(admin.ModelAdmin):
    inlines = [SuperheroPowersInline]

class EnemyAdmin(admin.ModelAdmin):
    exclude = ["powers"]
    inlines = [EnemyPowersInline]

admin.site.register(Power, PowerAdmin) # register custom model
admin.site.register(Superhero, SuperHeroAdmin)
admin.site.register(Enemy, EnemyAdmin)
admin.site.register(City)
