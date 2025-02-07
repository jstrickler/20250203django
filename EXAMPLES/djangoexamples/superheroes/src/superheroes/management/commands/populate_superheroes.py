import os
import yaml
from django.core.management.base import BaseCommand
from superheroes.models import Superhero, Enemy, Power, City
from superheroes.models_plus import SuperheroPlus, EnemyPlus, PowerPlus, CityPlus

DATA_FILE_NAME = "superheroes.yaml"
MODELS =  Superhero, Enemy, Power, City
PLUS_MODELS = SuperheroPlus, EnemyPlus, PowerPlus, CityPlus

class Command(BaseCommand):
    help = "Populates the superhero database"

    def handle(self, *args, **options):
        self.populate(*MODELS)
        self.populate(*PLUS_MODELS)

    def populate(self, hero_model, enemy_model, power_model, city_model):
        current_folder = os.path.dirname(__file__)
        data_file_path = os.path.join(current_folder, DATA_FILE_NAME)
        with open(data_file_path) as sup_in:
            sup_data = yaml.load(sup_in, Loader=yaml.BaseLoader)

        for s in sup_data:
            self.stdout.write(f"Adding {s['name']}")

            # add city
            city_name = s['city']
            results = city_model.objects.filter(name=city_name)
            if results:
                city = results[0]
            else:
                city = city_model(name=s['city'])
                city.save()

            # add powers
            powers = []
            for power, desc in s['powers']:
                results = power_model.objects.filter(name=power)
                if results:
                    p = results[0]
                    powers.append(p)
                else:
                    p = power_model(name=power, description=desc)
                    p.save()
                powers.append(p)

            # add enemies
            enemies = []
            for enemy in s['enemies']:
                results = enemy_model.objects.filter(name=enemy)
                if not results:
                    e = enemy_model(name=enemy)
                    e.save()
                    enemies.append(e)

            sup = hero_model(
                name=s['name'],
                real_name=s['real name'],
                secret_identity=s['secret identity'],
                city=city,
            )
            sup.save()
            for power in powers:
                sup.powers.add(power)

            for enemy in enemies:
                sup.enemies.add(enemy)
            sup.save()

            self.stdout.write(
                self.style.SUCCESS('Successfully populated superheroes')
            )
