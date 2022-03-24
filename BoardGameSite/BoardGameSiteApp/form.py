from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
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

    # def clean(self):
    #     cleaned_data = super().clean()
    #     user_login = cleaned_data.get('user_login')
    #     password = cleaned_data.get('password')
    #     repeat_password = cleaned_data.get('repeat_password')
    #     try:
    #         check_user = User.objects.get(username=user_login)
    #     except ObjectDoesNotExist:
    #         if password == repeat_password:
    #             raise forms.ValidationError('Użytkownik o takim loginie już istnieje w bazie! Hasła nie są takie same!')
    #         else:
    #             raise forms.ValidationError('Użytkownik o takim loginie już istnieje w bazie!')
    #     if password == repeat_password:
    #         raise forms.ValidationError('Hasła nie są takie same!')


class ResetPasswordForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
