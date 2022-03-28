from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.db.models.query import EmptyQuerySet
from django.contrib.auth.models import User


from random import choice

from .models import Game, PublishingHouse, Category, Mechanic
from .form import GameAddForm, LoginForm, UserAddForm
from .filter import GameFilter


class LandingPage(View):
    def get(self, request):
        logged_user = request.user
        if logged_user.is_authenticated:
            return render(request, 'landing_page.html', {'logged_user': logged_user})
        return render(request, 'landing_page.html')


class SearchPageView(View):
    def get(self, request):
        return render(request, 'search_page.html')


class GameDetailsView(View):
    def get(self, request, id):
        game = Game.objects.get(id=id)
        ctx = {'game': game}
        return render(request, 'game_details.html', ctx)


class GameAddView(CreateView):
    def get(self, request):
        form = GameAddForm()
        return render(request, 'add-game.html', {'form': form})

    def post(self, request):
        form = GameAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            categories = form.cleaned_data['categories']
            mechanics = form.cleaned_data['mechanics']
            minimum_players = form.cleaned_data['minimum_players']
            maximum_players = form.cleaned_data['maximum_players']
            publishing_house = form.cleaned_data['publishing_house']
            publishing_house_input = PublishingHouse.objects.get(id=publishing_house)
            minimum_age = form.cleaned_data['minimum_age']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            game = Game(name=name,
                        minimum_players=minimum_players,
                        maximum_players=maximum_players, publishing_house=publishing_house_input, minimum_age=minimum_age, description=description, image=image)
            game.save()
            game.categories.add(*categories)
            game.mechanics.add(*mechanics)
            response = f'stworzono ucznia: {name} i dodano do bazy'
        else:
            response = f'Wprowadź poprawne dane'
        return render(
            request,
            'add-game.html',
            {
                'form': form,
                'response': response
            })


class PublishingHouseAddCreateView(CreateView):
    model = PublishingHouse
    fields = ['name']
    success_url = '/publishing_houses/'


class PublishingHouseListView(View):
    def get(self, request):
        if PublishingHouse.objects.all().exists():
            publishing_houses = PublishingHouse.objects.all()
            ctx = {'publishing_houses': publishing_houses}
        else:
            ctx = {'error_msg': "Nie ma żadnego wydawnictwa w systemie"}
        return render(request, "publishing_houses.html", ctx)


class MechanicAddCreateView(CreateView):
    model = Mechanic
    fields = ['name', 'name_pl', 'description']
    success_url = '/mechanics/'


class MechanicListView(View):
    def get(self, request):
        if Mechanic.objects.all().exists():
            mechanics = Mechanic.objects.all()
            ctx = {'mechanics': mechanics}
        else:
            ctx = {'error_msg': "Nie ma żadnej mechaniki w systemie"}
        return render(request, "mechanics.html", ctx)


class CategoryAddCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    success_url = '/categories/'


class CategoryListView(View):
    def get(self, request):
        if Category.objects.all().exists():
            categories = Category.objects.all()
            ctx = {'categories': categories}
        else:
            ctx = {'error_msg': "Nie ma żadnej kategorii w systemie"}
        return render(request, "categories.html", ctx)


def game_list(request):
    f = GameFilter(request.GET, queryset=Game.objects.all())
    return render(request, 'filter_page.html', {'filter': f})


<<<<<<< HEAD
from django.contrib.auth import login, authenticate
class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                login_error = f'Brak urzytkownika o takim loginie oraz haśle, spróbuj ponownie! {username} {password}'
                return render(request, 'login.html', {"form": form, "login_error": login_error})
            else:
                login(request, user)
                return redirect("/")


from django.contrib.auth import logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/")


class SignUpView(View):
    def get(self, request):
        form = UserAddForm()
        return render(request, 'user-add.html', {"form": form})

    def post(self, request):
        form = UserAddForm(request.POST)
        if form.is_valid():
            user_login = form.cleaned_data['user_login']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            mail = form.cleaned_data['mail']
            User.objects.create_user(username=user_login, password=password, first_name=first_name, last_name=last_name, email=mail)
            return redirect('/login/')
        return render(request, 'user-add.html', {"form": form})


class random_game(View):
    def get(self, request):
        games = Game.objects.all()
        games_ids = []
        for game in games:
            games_ids.append(game.id)
        random_id = choice(games_ids)
        game = Game.objects.get(id=random_id)
        return redirect(f'/game_details/{game.id}')