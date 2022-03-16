from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)


class Mechanics(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)


class PublishingHouse(models.Model):
    name = models.CharField(max_length=64)


class Game(models.Model):
    name = models.CharField(max_length=64)
    categories = models.ManyToManyField(Category)
    mechanics = models.ManyToManyField(Mechanics)
    minimum_players = models.SmallIntegerField()
    maximum_players = models.SmallIntegerField()
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)
    minimum_age = models.SmallIntegerField()

