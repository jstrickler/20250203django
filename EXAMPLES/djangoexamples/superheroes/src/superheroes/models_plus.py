from uuid import uuid4
import logging
from django.db import models

logging.basicConfig(
    filename='superheroes.log',
    level=logging.INFO,
)

class SuperheroPlusManager(models.Manager):
    def get_fliers(self):
        return self.filter(powers__name__icontains="fly")

class PowerPlus(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)

    class Meta:
        db_table = "powers_plus"

    def __str__(self):
        return self.name

class CityPlus(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=32)

    class Meta:
        db_table = "cities_plus"

    def __str__(self):
        return self.name

class EnemyPlus(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=32)
    powers = models.ManyToManyField(PowerPlus)

    class Meta:
        db_table = "enemies_plus"

    def __str__(self):
        return self.name

class SuperheroPlus(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=32)
    real_name = models.CharField(max_length=32)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(CityPlus, on_delete=models.CASCADE)
    powers = models.ManyToManyField(PowerPlus)
    enemies = models.ManyToManyField(EnemyPlus)
    objects = SuperheroPlusManager()

    def __str__(self):
        return self.name

    class Meta():
        db_table = "superheroes_plus"
        ordering = ['secret_identity']

    def get_brief_enemies(self):
        enemies = [e.name.split()[-1] for e in self.enemies.all()]
        return '/'.join(enemies)

    def save(self, *args, **kwargs):
        logging.info("Created superhero {}".format(self.name))
        super().save(*args, **kwargs)
        # do something else here as needed

