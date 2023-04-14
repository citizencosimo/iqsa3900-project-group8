from reviewertools.models import Review
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from groupproject.forms import Game

def ReviewIndexTest(request):
        context = {}
        return render(request, 'review/reviewindex.html', context)

def CreateReview(request, game_id):
        context = {}
        context["form"] = ReviewForm(request.POST or None, request.FILES or None)
        context["game"] = get_object_or_404(Game, pk=game_id)
        return render(request, 'review/view.html', context)


