from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PublisherForm, GameForm, DeveloperForm, GenreForm, PlatformForm, LanguageForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse
from groupproject.models import Game, Publisher, Developer, Platform, Genre, Language
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
    gamess = Game.objects.all()
    data = {}
    data['objects_list'] = games
    return render(request, template_name, data)

def PublisherList(request, template_name='data/publisher_list.html'):
    publishers = Publisher.objects.all()
    data = {}
    data['objects_list'] = publishers
    return render(request, template_name, data)

def ViewPublisher(request, pk, template_name='data/publisher/publisher.html'):
    context={}
    publisher=get_object_or_404(Publisher, pk=pk)
    context['publisher'] = publisher
    return render(request, template_name, context)

def UpdatePublisher(request, pk, template_name='data/publisher/update.html'):
    context = {}
    publisher = get_object_or_404(Publisher, pk=pk)
    context['publisher'] = publisher
    form = PublisherForm(request.POST or None, instance=publisher)
    context['form'] = form
    if form.is_valid():
        form.save()
        return redirect('publisher_list')
    return render(request, template_name, context)


def DeletePublisher(request, pk, template_name='data/publisher/delete.html'):
    context={}
    context['publisher'] = get_object_or_404(Publisher, pk=pk)
    return render(request, template_name, context)


def ViewDeveloper(request, pk, template_name='data/developer/developer.html'):
    context={}
    developer=get_object_or_404(Developer, pk=pk)
    context['developer'] = developer
    return render(request, template_name, context)

def UpdateDeveloper(request, pk, template_name='data/developer/update.html'):
    context = {}
    developer = get_object_or_404(Publisher, pk=pk)
    context['developer'] = developer
    form = DeveloperForm(request.POST or None, instance=developer)
    context['form'] = form
    if form.is_valid():
        form.save()
        return redirect('developer_list')
    return render(request, template_name, context)


def DeleteDeveloper(request, pk, template_name='data/developer/delete.html'):
    context={}
    context['developer'] = get_object_or_404(Developer, pk=pk)
    return render(request, template_name, context)

def DeveloperList(request, template_name='data/developer_list.html'):
    developers = Developer.objects.all()
    data = {}
    data['objects_list'] = developers
    return render(request, template_name, data)
