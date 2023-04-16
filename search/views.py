from django.shortcuts import render
from django.http import HttpResponse
from groupproject.models import Game


def search(request):
    query = request.GET.get('q', '')
    games = Game.objects.filter(title__contains=query)
    # for game in games:
    #     print(game.title)
    #     print(game.release_date)
    context = {
        'query': query,
        'games': games,
    }
    return render(request, 'search.html', context)
