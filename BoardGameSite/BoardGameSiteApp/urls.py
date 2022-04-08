"""BoardGameSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from BoardGameSiteApp import views


urlpatterns = [
    path('', views.LandingPage.as_view(), name="index"),
    path('add_game/', views.GameAddView.as_view(), name="add-game"),
    path('add_category/', views.CategoryAddCreateView.as_view(), name="add-category"),
    path('categories/', views.CategoryListView.as_view(), name="categories"),
    path('add_mechanic/', views.MechanicAddCreateView.as_view(), name="add-mechanic"),
    path('mechanics/', views.MechanicListView.as_view(), name="mechanics"),
    path('add_publishing_house/', views.PublishingHouseAddCreateView.as_view(), name="add-publishing-house"),
    path('publishing_houses/', views.PublishingHouseListView.as_view(), name="publishing-houses"),
    path('game_details/<int:id>/', views.GameDetailsView.as_view(), name="game-details"),
    path('search/', views.GameList.as_view(), name="search"),
    path('shelf_search/<int:id>/', views.GameListShelfView.as_view(), name="shelf-search"),
    path('shelves_search/', views.GameListShelvesView.as_view(), name="shelves-search"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('sign_up/', views.SignUpView.as_view(), name="sign-up"),
    path('random_game/', views.RandomGame.as_view(), name="random-game"),
    path('random_game_but/', views.RandomGamesListView.as_view(), name="random-game-but"),
    path('random_game_shelf/<int:shelf_id>/', views.RandomGameShelfView.as_view(), name="random-game-shelf"),
    path('random_game_shelf_but/<int:shelf_id>/', views.RandomGamesShelfListView.as_view(), name="random-game-shelf-but"),
    path('shelves/', views.ShelvesView.as_view(), name="shelves"),
    path('delete_game_from_shelf/<int:shelf_id>/<int:game_id>/', views.DeleteGameFromShelfView.as_view(), name="delete-game-from-shelf"),
    path('delete_from_shelf_game/<int:shelf_id>/<int:game_id>/', views.DeleteFromShelfGameView.as_view(), name="delete-from-shelf-game"),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('edit_shelf/<int:id>/', views.ShelfEditView.as_view(), name='edit-shelf'),
    path('delete_shelf/<int:id>/', views.ShelfDeleteView.as_view(), name='delete-shelf'),
    path('move_game/<int:shelf_id>/<int:game_id>/', views.MoveGameView.as_view(), name="move-game"),
]
