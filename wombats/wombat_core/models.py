import uuid
from django.db import models

# Create your models here.

class Wombat(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=32)
