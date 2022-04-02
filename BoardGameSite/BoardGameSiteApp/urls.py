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
from django.contrib import admin
from django.urls import path
from BoardGameSiteApp import views
from django.conf import settings
from django.conf.urls.static import static


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
    path('search/', views.game_list, name="search"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('sign_up/', views.SignUpView.as_view(), name="sign-up"),
    path('random_game/', views.random_game.as_view(), name="random-game"),
    path('random_game_but/', views.RandomGamesListView.as_view(), name="random-game-but"),
    path('shelves/', views.ShelvesView.as_view(), name="shelves"),
    path('shelf/<int:shelf_id>', views.ShelfDetailsView.as_view(), name="shelf-details"),
    path('delete_game_from_shelf/<int:shelf_id>/<int:game_id>/', views.DelateGameFromShelfView.as_view(), name="delete-from-shelf"),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
]