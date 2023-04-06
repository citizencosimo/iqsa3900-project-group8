from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PublisherForm, GameForm, DeveloperForm, GenreForm, PlatformForm, LanguageForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse
from groupproject.models import Game
from django.urls import reverse_lazy


def ListView(request):
    context = {
        'names': ['game', 'developer', 'publisher', 'platform', 'genre', 'language']
    }
    return render(request, 'data/list.html', context)


def CreatePublisher(request):
    context = {}
    form = PublisherForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'data/forms/publisher_a.html', context)


def CreateDeveloper(request):
    context = {}
    form = DeveloperForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'data/forms/add_developer.html', context)


def CreatePlatform(request):
    context = {}
    form = PlatformForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'data/forms/add_platform.html', context)


def CreateGenre(request):
    context = {}
    form = GenreForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'data/forms/add_genre.html', context)


def CreateLanguage(request):
    context = {}
    form = LanguageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'data/forms/add_language.html', context)


def CreateGame(request):
    context = {}
    form = GameForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'data/forms/add_game.html', context)

def ViewGame(request, pk, template_name='data/game/game.html'):
    context={}
    game=get_object_or_404(Game, pk=pk)
    context['game'] = game
    return render(request, template_name, context)

def UpdateGame(request, pk, template_name='data/game/update.html'):
    context = {}
    game = get_object_or_404(Game, pk=pk)
    context['game'] = game
    form = GameForm(request.POST or None, instance=game)
    context['form'] = form
    if form.is_valid():
        form.save()
        return redirect('game_list')
    return render(request, template_name, context)


def DeleteGame(request, pk, template_name='data/game/delete.html'):
    context={}
    context['game'] = get_object_or_404(Game, pk=pk)
    return render(request, template_name, context)

def GameList(request, template_name='data/game_list.html'):
    games = Game.objects.all()
    data = {}
    data['objects_list'] = games
    return render(request, template_name, data)
