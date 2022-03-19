from django import forms
from .models import Game, Mechanic,  Category, PublishingHouse


class GameAddForm(forms.Form):
    name = forms.CharField(label='Nazwa gry', max_length=64)
    categories = forms.MultipleChoiceField(label="Kategorie:", widget=forms.CheckboxSelectMultiple)
    mechanics = forms.MultipleChoiceField(label="Mechaniki:", widget=forms.CheckboxSelectMultiple)
    minimum_players = forms.IntegerField(label="Minimalna liczba graczy:")
    maximum_players = forms.IntegerField(label="Maksymalna liczba graczy:")
    publishing_house = forms.ChoiceField(label="Wydawnictwo:")
    minimum_age = forms.IntegerField(label="Wiek minimalny")
    description = forms.CharField(label='Opis gry')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        category_choices = tuple([(category.id, f'{category.name}') for category in Category.objects.all()])
        self.fields['categories'].choices = category_choices
        mechanic_choices = tuple([(mechanic.id, f'{mechanic.name} ({mechanic.name_pl})') for mechanic in Mechanic.objects.all()])
        self.fields['mechanics'].choices = mechanic_choices
        publishing_house_choices = tuple([(publishing_house.id, f'{publishing_house.name}') for publishing_house in PublishingHouse.objects.all()])
        self.fields['publishing_house'].choices = publishing_house_choices
