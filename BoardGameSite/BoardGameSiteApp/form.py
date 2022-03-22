from django import forms
from .models import Game, Mechanic,  Category, PublishingHouse


class GameAddForm(forms.Form):
    name = forms.CharField(label='Nazwa gry', max_length=64)
    categories = forms.MultipleChoiceField(label="Kategorie:", widget=forms.CheckboxSelectMultiple)
    mechanics = forms.MultipleChoiceField(label="Mechaniki:", widget=forms.CheckboxSelectMultiple)
    minimum_players = forms.IntegerField(label="Minimalna liczba graczy:")
    maximum_players = forms.IntegerField(label="Maksymalna liczba graczy:")
    publishing_house = forms.ChoiceField(label="Wydawnictwo:")
    minimum_age = forms.IntegerField(label="Wiek minimalny:")
    description = forms.CharField(label='Opis gry:')
    image = forms.ImageField(label='Zdjęcie gry:')
