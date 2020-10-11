# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from six import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    from_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Asset(models.Model):
    name = models.CharField(max_length=100, unique=True)
    from_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
