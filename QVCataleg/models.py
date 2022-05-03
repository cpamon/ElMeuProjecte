from asyncio.windows_events import NULL
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.urls import reverse


class Aplicacio(models.Model):
    nom =     models.CharField(max_length=100)
    laUrl =   models.CharField(max_length=100)
    grupPermis =   models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nom
    class Meta:
        db_table = "aplicacio"


""" class RefMapaWMS(models.Model):
    tipus   =   models.CharField(max_length=20)
    nom     =   models.CharField(max_length=100)
    descripcio      = models.TextField(null=True)
    pUrl    =   models.CharField(max_length=200)
    urlCapabilities    =   models.CharField(max_length=200, default='X', null=True)
    matrixSet = models.CharField(max_length=30, null=True)
    format = models.CharField(max_length=20, null=True)
    foto = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    mapa_actual = models.BooleanField(default=False)

    def __str__(self):
        return self.nom """

class RefCapa(models.Model):
    codiCapa = models.CharField(max_length=100)
    nomCapa = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    tipus = models.CharField(max_length=200)
    matrixSet = models.CharField(max_length=30, null=True)
    format = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.codiCapa

class RefMapa(models.Model):
    codiMapa = models.CharField(max_length=100, null=True)
    nom = models.CharField(max_length=200, null=True)
    tipus   =   models.CharField(max_length=20, null=True)
    descripcio      = models.TextField(null=True)
    pUrl    =   models.CharField(max_length=200, null=True)
    urlCapabilities    =   models.CharField(max_length=200, default='X', null=True)
    matrixSet = models.CharField(max_length=30, null=True)
    format = models.CharField(max_length=20, null=True)
    foto = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    mapa_actual = models.BooleanField(default=False)
    mapa_compost = models.BooleanField(default=False)

    def __str__(self):
        return self.codiMapa

class RefMapaCapa(models.Model):
    codiMapa = models.CharField(max_length=5)
    codiCapa = models.CharField(max_length=5)

    def __str__(self):
        return self.codiMapa

class Pokemon(models.Model):
    nom     =   models.CharField(max_length=20)
    tipus   =   models.CharField(max_length=100)

    def __str__(self):
        return self.nom