from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from accounts.mixins import StaffRequiredMixin
from reviewertools.models import Review
from .forms import PublisherForm, GameForm, DeveloperForm, GenreForm, PlatformForm, LanguageForm, ImageForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from groupproject.models import Game, Publisher, Developer, Platform, Genre, Language, Image
from django.urls import reverse_lazy
from django.contrib import messages

def DatabaseLinks(request):
    mixin = StaffRequiredMixin()


    context = {
        'site_names': [('games', 'Game List'),
                       ('developers', 'Developer List'),
                       ('publishers', 'Publisher List'),
                       ('platforms', 'Platform List'),
                       ('genres', 'Genre List'),
                       ('languages', 'Language List'),
                       ('add_language', 'Add Language'),
                       ('add_genre', 'Add Genre'),
        ]

    }
    return render(request, 'data/list.html', context)


def CreatePublisher(request):
    context = {}
    form = PublisherForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added')
        return redirect('publisher_list')
    context['form'] = form
    return render(request, 'data/forms/add_publisher.html', context)


def CreateDeveloper(request):
    context = {}
    form = DeveloperForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added')
        return redirect('developer_list')
    context['form'] = form
    return render(request, 'data/forms/add_developer.html', context)


def CreatePlatform(request):
    context = {}
    form = PlatformForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added')
        return redirect('platform_list')
    context['form'] = form
    return render(request, 'data/forms/add_platform.html', context)


def CreateGenre(request):
    context = {}
    form = GenreForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.success(request, 'Successfully Added')
        form.save()
        return redirect('database_links')
    context['form'] = form
    return render(request, 'data/forms/add_genre.html', context)


def CreateLanguage(request):
    context = {}
    form = LanguageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.success(request, 'Successfully Added')
        form.save()
        return redirect('database_links')
    context['form'] = form
    return render(request, 'data/forms/add_language.html', context)

def GenreList(request, template_name='data/genre_list.html'):
    print(Genre.objects.all())
    genres = Genre.objects.all()
    for genre in genres:
        print('genenen:', genre.pk)
    data = {}
    data['genres'] = genres
    return render(request, template_name, data)

def ViewGenre(request, pk, template_name='data/genre/genre.html'):
    context = {}
    genre = get_object_or_404(Genre, pk=pk)
    print('Genre:', genre)
    context['genre'] = genre
    return render(request, template_name, context)

def UpdateGenre(request, pk, template_name='data/genre/update.html'):
    context = {}
    genre = get_object_or_404(Genre, pk=pk)
    context['genre'] = genre
    form = GenreForm(request.POST or None, instance=genre)
    context['form'] = form
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Updated')
        return redirect('genre_list')
    return render(request, template_name, context)


def LanguageList(request, template_name='data/language_list.html'):
    print(Language.objects.all())
    languages = Language.objects.all()
    data = {}
    data['languages'] = languages
    return render(request, template_name, data)


def ViewLanguage(request, pk, template_name='data/language/language.html'):
    context = {}
    language = get_object_or_404(Language, pk=pk)
    print('Language:', language)
    context['language'] = language
    return render(request, template_name, context)


def UpdateLanguage(request, pk, template_name='data/language/update.html'):
    context = {}
    language = get_object_or_404(Language, pk=pk)
    context['language'] = language
    form = LanguageForm(request.POST or None, instance=language)
    context['form'] = form
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Updated')
        return redirect('language_list')
    return render(request, template_name, context)

def DeleteLanguage(request, pk, template_name='data/language/delete.html'):
    context = {}
    obj = get_object_or_404(Language, pk=pk)
    context['language'] = obj
    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('database_links')
    return render(request, template_name, context)

def CreateGame(request):
    context = {}
    form = GameForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added')
        return redirect('game_list')
    context['form'] = form
    return render(request, 'data/forms/add_game.html', context)


def ViewGame(request, pk, template_name='data/game/game.html'):
    context = {}
    game = get_object_or_404(Game, pk=pk)
    if request.user.is_staff or request.user.is_superuser:
        reviews = Review.objects.filter(game=game)
    else:
        reviews = Review.objects.filter(game=game, is_flagged=False)
    context['reviews'] = reviews
    context['game'] = game
    return render(request, template_name, context)

def DeleteGenre(request, pk, template_name='data/genre/delete.html'):
    context = {}
    obj = get_object_or_404(Genre, pk=pk)
    context['genre'] = obj
    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('database_links')
    return render(request, template_name, context)

def UpdateGame(request, pk, template_name='data/game/update.html'):
    context = {}
    game = get_object_or_404(Game, pk=pk)
    context['game'] = game
    form = GameForm(request.POST or None, request.FILES or None, instance=game)
    context['form'] = form
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Updated')
        return redirect('game_list')
    return render(request, template_name, context)


def DeleteGame(request, pk, template_name='data/game/delete.html'):
    context = {}
    obj = get_object_or_404(Game, pk=pk)
    context['game'] = obj
    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('database_links')
    return render(request, template_name, context)


def GameList(request, template_name='data/game_list.html'):
    games = Game.objects.all()
    data = {}
    data['games'] = games
    return render(request, template_name, data)


def PublisherList(request, template_name='data/publisher_list.html'):
    publishers = Publisher.objects.all()
    data = {}
    data['objects_list'] = publishers
    return render(request, template_name, data)


def ViewPublisher(request, pk, template_name='data/publisher/publisher.html'):
    context = {}
    publisher = get_object_or_404(Publisher, pk=pk)
    context['publisher'] = publisher
    return render(request, template_name, context)


def UpdatePublisher(request, pk, template_name='data/publisher/update.html'):
    context = {}
    publisher = get_object_or_404(Publisher, pk=pk)
    context['publisher'] = publisher
    form = PublisherForm(request.POST or None, instance=publisher)

    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Updated')
        return redirect('publisher_list')
    context['form'] = form
    return render(request, template_name, context)


def DeletePublisher(request, pk, template_name='data/publisher/delete.html'):
    context = {}
    obj = get_object_or_404(Publisher, pk=pk)
    context['publisher'] = obj
    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('database_links')
    return render(request, template_name, context)


def ViewDeveloper(request, pk, template_name='data/developer/developer.html'):
    context = {}
    developer = get_object_or_404(Developer, pk=pk)
    context['developer'] = developer
    return render(request, template_name, context)


def UpdateDeveloper(request, pk, template_name='data/developer/update.html'):
    context = {}
    developer = get_object_or_404(Developer, pk=pk)
    context['developer'] = developer
    form = DeveloperForm(request.POST, instance=developer)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Updated')
        return redirect('developer_list')
    context['form'] = form
    return render(request, template_name, context)


def DeleteDeveloper(request, pk, template_name='data/developer/delete.html'):
    context = {}
    obj = get_object_or_404(Developer, pk=pk)
    context['developer'] = obj
    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('database_links')
    return render(request, template_name, context)


def DeveloperList(request, template_name='data/developer_list.html'):
    developers = Developer.objects.all()
    data = {}
    data['objects_list'] = developers
    return render(request, template_name, data)


def ViewPlatform(request, pk, template_name='data/platform/platform.html'):
    context = {}
    platform = get_object_or_404(Platform, pk=pk)
    context['platform'] = platform
    return render(request, template_name, context)


def UpdatePlatform(request, pk, template_name='data/platform/update.html'):
    context = {}
    platform = get_object_or_404(Platform, pk=pk)
    context['developer'] = platform
    form = PlatformForm(request.POST or None, instance=platform)
    context['form'] = form
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Updated')
        return redirect('platform_list')
    return render(request, template_name, context)


def DeletePlatform(request, pk, template_name='data/platform/delete.html'):
    context = {}
    obj = get_object_or_404(Platform, pk=pk)
    context['developer'] = obj
    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('database_links')
    return render(request, template_name, context)


def PlatformList(request, template_name='data/platform_list.html'):
    platforms = Platform.objects.all()
    data = {}
    data['objects_list'] = platforms
    return render(request, template_name, data)

def image_upload_view(request):
    """Image upload view."""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def ModifiedSearchRequest(request):
    context = {}
    query = request.GET.get('query')
    if query != "":
        result = Game.objects.filter(title__contains=query)
        context['results'] = list(result.values())
        context['string'] = [(game.__str__(), game.pk) for game in result]
    else:
        context['results'] = []

    return JsonResponse(context)

def HomePageDetailView(request):
    context = {}
    query = request.GET.get('id')
    result = get_object_or_404(Game, pk=query)
    # print(result.__str__())
    if result:
        context = {
            'gameid' : result.pk,
            'title': result.title,
            'publisher': str(result.publisher),
            'developer': str(result.developer),
            'rating': result.rating,
            'gamesum': result.description,
            'release_date': str(result.release_date)
        }
    return JsonResponse(context)

