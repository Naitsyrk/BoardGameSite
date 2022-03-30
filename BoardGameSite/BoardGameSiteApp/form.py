from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import Game, Mechanic,  Category, PublishingHouse


class GameAddForm(forms.Form):
    name = forms.CharField(label='Nazwa gry', max_length=64)
    categories = forms.ModelMultipleChoiceField(label="Kategorie:", queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    mechanics = forms.ModelMultipleChoiceField(label="Mechaniki:", queryset=Mechanic.objects.all(), widget=forms.CheckboxSelectMultiple)
    minimum_players = forms.IntegerField(label="Minimalna liczba graczy:")
    maximum_players = forms.IntegerField(label="Maksymalna liczba graczy:")
    publishing_house = forms.ModelChoiceField(label="Wydawnictwo:", queryset=PublishingHouse.objects.all())
    minimum_age = forms.IntegerField(label="Wiek minimalny:")
    description = forms.CharField(label='Opis gry:')
    image = forms.ImageField(label='Zdjęcie gry:')


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class UserAddForm(forms.Form):
    user_login = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    first_name = forms.CharField(label="Imię:")
    last_name = forms.CharField(label="Nazwisko:")
    mail = forms.CharField(label="Mail:", validators=[EmailValidator])



class ResetPasswordForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
