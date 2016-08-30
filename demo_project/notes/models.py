# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    from_country = models.ForeignKey(Country)

    def __str__(self):
        return self.name
