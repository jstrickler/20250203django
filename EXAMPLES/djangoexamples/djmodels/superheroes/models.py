from uuid import uuid4
from django.db import models

class Power(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=512)

    class Meta:
        db_table = "powers"

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        db_table = "cities"
        # verbose_name ="city"
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name


class Enemy(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    powers = models.ManyToManyField(Power)

    class Meta:
        db_table = "enemies"
        verbose_name_plural = "enemies"

    def __str__(self):
        return self.name


class Superhero(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    real_name = models.CharField(max_length=32)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)

    class Meta:
        db_table = "superheroes"

    def __str__(self):
        return self.name
