from uuid import uuid4
from django.db import models


class Power(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "powers"


class City(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "cities"

class Enemy(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "enemies"

class Superhero(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    real_name = models.CharField(max_length=32)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "superheroes"
