from django.db import models

# Create your models here.
class Animals(models.Model):
    nomAnimal = models.CharField(max_length=20)
    especie = models.CharField(max_length=40)

    def __str__(self):
        return self.nomAnimal