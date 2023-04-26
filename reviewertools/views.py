from reviewertools.models import Review
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from groupproject.forms import Game

def ReviewIndexTest(request):
        context = {}
        return render(request, 'review/reviewindex.html', context)

def CreateReview(request, game_id):
        context = {}
        game = get_object_or_404(Game, pk=game_id)
        context["game"] = game

        form = ReviewForm(request.POST or None, request.FILES or None)
        context["form"] = form

        if form.is_valid():
                form.instance.game = game
                form.instance.user = request.user
                cleaned_data = form.cleaned_data
                form.save(cleaned_data)

        else:
                print('failure')

        return render(request, 'review/view.html', context)


