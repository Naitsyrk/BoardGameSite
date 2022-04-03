from django.db import models
from django.contrib.auth.models import User


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
    categories = models.ManyToManyField(Category, through='GameCategory')
    mechanics = models.ManyToManyField(Mechanic, through="GameMechanic")
    minimum_players = models.SmallIntegerField()
    maximum_players = models.SmallIntegerField()
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)
    minimum_age = models.SmallIntegerField()
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.name


class GameMechanic(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)


class GameCategory(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Shelf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    games = models.ManyToManyField(Game, through='ShelfGame')

    def __str__(self):
        return self.name


class ShelfGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
