from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.db.models.query import EmptyQuerySet
from django.contrib.auth.models import User


from random import choice, sample

from .models import Game, PublishingHouse, Category, Mechanic, ShelfGame, Shelf
from .form import GameAddForm, LoginForm, UserAddForm, AddGameToShelfForm
from .filter import GameFilter, RandomGameFilter


class LandingPage(View):
    def get(self, request):
        logged_user = request.user
        last_added_games = Game.objects.all().order_by('-id')[:3]
        first_game = last_added_games.first()
        other_games = last_added_games[1:]
        ctx = {"other_games": other_games, 'first_game': first_game}
        if logged_user.is_authenticated:
            ctx['logged_user'] = logged_user
            return render(request, 'landing_page.html', ctx)
        return render(request, 'landing_page.html', ctx)


class GameDetailsView(View):
    def get(self, request, id):
        logged_user = request.user
        game = Game.objects.get(id=id)
        ctx = {'game': game}
        form = AddGameToShelfForm()
        form.fields['shelf'].queryset = Shelf.objects.filter(user=logged_user)
        ctx['form'] = form
        if logged_user.is_authenticated:
            ctx['logged_user'] = logged_user
        shelves = Shelf.objects.filter(user=logged_user).filter(games=game)
        ctx['shelves'] = shelves
        return render(request, 'game_details.html', ctx)

    def post(self, request, id):
        logged_user = request.user
        game = Game.objects.get(id=id)
        ctx = {'game': game}
        if logged_user.is_authenticated:
            ctx['logged_user'] = logged_user
            form = AddGameToShelfForm(request.POST)
            form.fields['shelf'].queryset = Shelf.objects.filter(user=logged_user)
            if form.is_valid():
                shelf = form.cleaned_data['shelf']
                shelf.games.add(game)
                ctx['form'] = form
                shelf.games.add(game)
        shelves = Shelf.objects.filter(user=logged_user).filter(games=game)
        ctx['shelves'] = shelves
        return render(request, 'game_details.html', ctx)


class GameAddView(CreateView):
    def get(self, request):
        form = GameAddForm()
        return render(request, 'add-game.html', {'form': form})

    def post(self, request):
        form = GameAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            response = f'stworzono grę: {name} i dodano do bazy'
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


class GameList(View):
    def get(self, request):
        f = GameFilter(request.GET, queryset=Game.objects.all())
        return render(request, 'filter_page.html', {'filter': f})

    def post(self, request):
        f = GameFilter(request.GET, queryset=Game.objects.all())
        init_name = request.POST.get('init_name')
        f.data = f.data.copy()
        f.data.setdefault('name', init_name)
        return render(request, 'filter_page.html', {'filter': f})


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
            new_user = User.objects.get(username=user_login)
            Shelf.objects.create(user=new_user, name="Posiadane")
            Shelf.objects.create(user=new_user, name="Wishlist")
            return redirect('/login/')
        return render(request, 'user-add.html', {"form": form})


class RandomGame(View):
    def get(self, request):
        games = Game.objects.all()
        games_ids = []
        for game in games:
            games_ids.append(game.id)
        random_id = choice(games_ids)
        game = Game.objects.get(id=random_id)
        return redirect(f'/game_details/{game.id}')


class RandomGamesListView(View):
    filter_class = RandomGameFilter

    def get(self, request):
        game_filter = self.filter_class(request.GET, queryset=Game.objects.all())
        game = game_filter.qs.order_by('?').first()
        return render(request, 'random_filter_page.html', {'filter': game_filter, 'game': game})

      
class ShelvesView(View):
    template = 'shelves.html'

    def get(self, request):
        logged_user = request.user
        if logged_user.is_authenticated:
            shelves = Shelf.objects.filter(user=logged_user)
            return render(request, self.template, {
                'logged_user': logged_user,
                'shelves': shelves
            })
        else:
            return redirect('/login/')

    def post(self, request):
        logged_user = request.user
        shelf_name = request.POST.get('shelf_name')
        Shelf.objects.create(user=logged_user, name=shelf_name)
        shelves = Shelf.objects.filter(user=logged_user)
        return render(request, self.template, {
            'logged_user': logged_user,
            'shelves': shelves
        })


class ShelfDetailsView(View):
    def get(self, request, shelf_id):
        logged_user = request.user
        shelf = Shelf.objects.get(id=shelf_id)
        games = [game for game in shelf.games.all()]
        if logged_user.is_authenticated:
            return render(request, 'shelf_details.html', {
                'games': games,
                'logged_user': logged_user,
                'shelf': shelf
            })


class DeleteGameFromShelfView(View):
    def get(self, request, shelf_id, game_id):
        shelf = Shelf.objects.get(id=shelf_id)
        game = Game.objects.get(id=game_id)
        shelf.games.remove(game)
        return redirect(f'/game_details/{game.id}')


class DeleteFromShelfGameView(View):
    def get(self, request, shelf_id, game_id):
        shelf = Shelf.objects.get(id=shelf_id)
        game = Game.objects.get(id=game_id)
        shelf.games.remove(game)
        return redirect(f'/shelf/{shelf.id}')


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')


class ShelfEditView(View):
    def get(self, request, id):
        shelf = Shelf.objects.get(id=id)
        return render(request,
                      'edit_shelf.html',
                      {
                          'shelf': shelf,
                      })

    def post(self, request, id):
        shelf = Shelf.objects.get(id=id)
        name = request.POST.get('name')
        shelf.name = name
        shelf.save()
        return redirect('/shelves/')


class ShelfDeleteView(View):
    def get(self, request, id):
        shelf = Shelf.objects.get(id=id).delete()
        return redirect('/shelves/')


