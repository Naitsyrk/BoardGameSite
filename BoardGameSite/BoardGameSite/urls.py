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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingPage.as_view(), name="index"),
    # path('game_list/', views.GamelistView, name="game-list"),
    # path('game_add/', views.GameAddView, name="game-add"),
    # path('search/', views.GameAddView, name="search"),
    # path('game_details/', views.GameDetailsView, name="game-details"),
    # path('login/', Login.as_view(), name="login"),
    # path('logout/', Logout.as_view(), name="logout"),
    # path('sing_up/', Sign_upView.as_view(), name="sing-up"),

]
