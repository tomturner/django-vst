from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=128)


class Title(models.Model):
    title = models.CharField(max_length=6)


class Contact(models.Model):
    title = models.ForeignKey(Title)
    surname = models.CharField(max_length=32)
    forename = models.CharField(max_length=32)
    country = models.ForeignKey(Country)

    type = models.IntegerField()
