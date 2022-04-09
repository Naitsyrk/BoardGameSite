from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout

from random import choice

from .models import Game, PublishingHouse, Category, Mechanic, Shelf
from .form import GameAddForm, LoginForm, UserAddForm, AddGameToShelfForm
from .filter import GameFilter, RandomGameFilter


class LandingPage(View):
    def get(self, request):
        logged_user = request.user
        last_added_games = Game.objects.all().order_by('-id')[:3]
        first_game = last_added_games.first()
        other_games = last_added_games[1:]
        ctx = {"other_games": other_games, 'first_game': first_game, 'logged_user': logged_user}
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
        form.fields['shelf'].queryset = Shelf.objects.filter(user=logged_user).exclude(games=game).order_by('name')
        ctx['form'] = form
        if logged_user.is_authenticated:
            ctx['logged_user'] = logged_user
        shelves = Shelf.objects.filter(user=logged_user).filter(games=game).order_by('name')
        ctx['shelves'] = shelves
        return render(request, 'game_details.html', ctx)

    def post(self, request, id):
        logged_user = request.user
        game = Game.objects.get(id=id)
        ctx = {'game': game}
        if logged_user.is_authenticated:
            ctx['logged_user'] = logged_user
            form = AddGameToShelfForm(request.POST)
            form.fields['shelf'].queryset = Shelf.objects.filter(user=logged_user).exclude(games=game).order_by('name')
            if form.is_valid():
                shelf = form.cleaned_data['shelf']
                shelf.games.add(game)
                ctx['form'] = form
                shelf.games.add(game)
        shelves = Shelf.objects.filter(user=logged_user).filter(games=game).order_by('name')
        ctx['shelves'] = shelves
        return render(request, 'game_details.html', ctx)


class GameAddView(CreateView):
    def get(self, request):
        logged_user = request.user
        form = GameAddForm()
        return render(request, 'add-game.html', {'form': form, 'logged_user': logged_user})

    def post(self, request):
        logged_user = request.user
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
                'response': response,
                'logged_user': logged_user
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
        logged_user = request.user
        f = GameFilter(request.GET, queryset=Game.objects.all())
        return render(request, 'filter_page.html', {'filter': f, 'logged_user': logged_user})

    def post(self, request):
        logged_user = request.user
        f = GameFilter(request.GET, queryset=Game.objects.all())
        init_name = request.POST.get('init_name')
        f.data = f.data.copy()
        f.data.setdefault('name', init_name)
        return render(request, 'filter_page.html', {'filter': f, 'logged_user': logged_user})


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
        logged_user = request.user
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
        logged_user = request.user
        game_filter = self.filter_class(request.GET, queryset=Game.objects.all())
        game = game_filter.qs.order_by('?').first()
        return render(request, 'random_filter_page.html', {'filter': game_filter, 'game': game, 'logged_user': logged_user})

      
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


class DeleteGameFromShelfView(View):
    def get(self, request, shelf_id, game_id):
        logged_user = request.user
        shelf = Shelf.objects.get(id=shelf_id)
        game = Game.objects.get(id=game_id)
        shelf.games.remove(game)
        return redirect(f'/game_details/{game.id}')


class DeleteFromShelfGameView(View):
    def get(self, request, shelf_id, game_id):
        logged_user = request.user
        shelf = Shelf.objects.get(id=shelf_id)
        game = Game.objects.get(id=game_id)
        shelf.games.remove(game)
        return redirect(f'/shelf_search/{shelf.id}')


class About(View):
    def get(self, request):
        logged_user = request.user
        return render(request, 'about.html', {'logged_user': logged_user})


class Contact(View):
    def get(self, request):
        logged_user = request.user
        return render(request, 'contact.html', {'logged_user': logged_user})


class ShelfEditView(View):
    def get(self, request, id):
        logged_user = request.user
        shelf = Shelf.objects.get(id=id)
        return render(request,
                      'edit_shelf.html',
                      {
                          'shelf': shelf,
                          'logged_user': logged_user
                      })

    def post(self, request, id):
        logged_user = request.user
        shelf = Shelf.objects.get(id=id)
        name = request.POST.get('name')
        shelf.name = name
        shelf.save()
        return redirect('/shelves/')


class ShelfDeleteView(View):
    def get(self, request, id):
        logged_user = request.user
        shelf = Shelf.objects.get(id=id).delete()
        return redirect('/shelves/')


class GameListShelfView(View):
    def get(self, request, id):
        logged_user = request.user
        shelf = Shelf.objects.get(id=id)
        f = GameFilter(request.GET, queryset=shelf.games.all())
        form = AddGameToShelfForm()
        form.fields['shelf'].queryset = Shelf.objects.filter(user=logged_user).exclude(name=shelf.name)
        ctx ={
                'filter': f,
                'shelf': shelf,
                'logged_user': logged_user,
                "form": form,
            }
        if len(f.queryset) == 0:
            ctx['response'] = "Brak gry na półce"
        return render(
            request,
            'filter_shelf.html',
            ctx,
            )

class GameListShelvesView(View):
    def get(self, request):
        logged_user = request.user
        games = Game.objects.filter(shelf__user=logged_user).distinct()
        f = GameFilter(request.GET, queryset=games)
        return render(request, 'filter_shelves.html', {'filter': f})

    def post(self, request):
        logged_user = request.user
        games = Game.objects.filter(shelf__user=logged_user).distinct()
        f = GameFilter(request.GET, queryset=games)
        init_name = request.POST.get('init_name')
        f.data = f.data.copy()
        f.data.setdefault('name', init_name)
        return render(request, 'filter_shelves.html', {'filter': f})


class MoveGameView(View):
    def post(self, request, game_id, shelf_id):
        logged_user = request.user
        game = Game.objects.get(id=game_id)
        form = AddGameToShelfForm(request.POST)
        init_shelf = Shelf.objects.get(id=shelf_id)
        if form.is_valid():
            new_shelf = form.cleaned_data['shelf']
            new_shelf.games.add(game)
            init_shelf.games.remove(game)
        return redirect(f'/shelf_search/{init_shelf.id}/')


class RandomGameShelfView(View):
    def get(self, request, shelf_id):
        logged_user = request.user
        games = Game.objects.filter(shelf__user=logged_user).filter(shelf__id=shelf_id).distinct()
        games_ids = []
        for game in games:
            games_ids.append(game.id)
        random_id = choice(games_ids)
        game = Game.objects.get(id=random_id)
        return redirect(f'/game_details/{game.id}')


class RandomGamesShelfListView(View):
    filter_class = RandomGameFilter

    def get(self, request, shelf_id):
        logged_user = request.user
        shelf = Shelf.objects.get(id=shelf_id)
        games = Game.objects.filter(shelf__user=logged_user).filter(shelf__id=shelf_id).distinct()
        game_filter = self.filter_class(request.GET, queryset=games)
        game = game_filter.qs.order_by('?').first()
        return render(request, 'random_filter_shelf.html', {'filter': game_filter, 'game': game, 'logged_user': logged_user, 'shelf': shelf})
