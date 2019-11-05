from django.db import models
from django.utils import timezone


class Menu(models.Model):
    season = models.CharField(max_length=20)  # Required Field
    items = models.ManyToManyField('Item', related_name='items')  # Required Field
    created_date = models.DateTimeField(default=timezone.now)  # Hidden Field
    expiration_date = models.DateField()  # Required Field

    def __str__(self):
        return self.season


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    chef = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    created_date = models.DateTimeField(default=timezone.now)
    standard = models.BooleanField(default=False)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.name
