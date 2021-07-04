# -*- encoding: utf-8 -*-
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    from_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=100, unique=True)
    from_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
