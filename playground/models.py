from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    price = models.IntegerField
    stock = models.IntegerField

    def __str__(self):
        return self.title

class Collection(models.Model):
    title = models.CharField(max_length=20)

class Cart(models.Model):
    product = [Product]
    created_at = models.DateField

class Customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

class Order(models.Model):
    customer = Customer
    created_at = models.DateField