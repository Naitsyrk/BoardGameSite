from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name


class Mechanic(models.Model):
    name = models.CharField(max_length=64)
    name_pl = models.CharField(max_length=64)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class PublishingHouse(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=64, unique=True)
    categories = models.ManyToManyField(Category)
    mechanics = models.ManyToManyField(Mechanic)
    minimum_players = models.SmallIntegerField()
    maximum_players = models.SmallIntegerField()
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)
    minimum_age = models.SmallIntegerField()
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="media", null=True)

    def __str__(self):
        return self.name

