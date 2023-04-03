from django.shortcuts import render
from .forms import PublisherForm, GameForm, DeveloperForm, GenreForm, PlatformForm, LanguageForm


def ListView(request):
    context = {
        'names': ['game', 'developer', 'publisher', 'platform', 'genre', 'language']
    }
    return render(request, 'data/list.html', context)

def CreatePublisher(request):
    context={}
    form = PublisherForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, 'data/forms/publisher_a.html', context)

def CreateDeveloper(request):
    context={}
    form = DeveloperForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'data/forms/add_developer.html', context)
def CreatePlatform(request):
    context={}
    form = PlatformForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'data/forms/add_platform.html.html', context)
def CreateGenre(request):
    context={}
    form = GenreForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, 'data/forms/add_genre.html', context)
def CreateLanguage(request):
    context={}
    form = LanguageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, 'data/forms/add_language.html', context)

def CreateGame(request):
    context = {}
    form = GameForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form;
    return render(request, 'data/forms/add_game.html', context)
