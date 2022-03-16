from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


class LandingPage(View):
    def get(self, request):
        return render(request, 'landing_page.html')

class SearchPageView(View):
    def get(self, request):
        return render(request, 'search_page.html')

