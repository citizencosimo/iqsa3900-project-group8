from datetime import time, datetime

from reviewertools.models import Review, ReviewTicket
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, ReviewTicket
from groupproject.forms import Game
from django.contrib import messages

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


def UpdateReview(request, review_id):
        context = {}
        review = get_object_or_404(Review, pk=review_id)
        if request.user.pk == review.user.pk:
                # game= review.game
                form = ReviewForm(request.POST or None, request.FILES or None, instance = review)
                context['form'] = form
                if form.is_valid():
                        # For later, to save an updated date
                        # edit_time = datetime.now().strftime("%d-%m-%Y at %H:%M:%S")
                        # form.instance.comment += "Edited on {}".format(edit_time);
                        cleaned_data = form.cleaned_data
                        form.save(cleaned_data)
                        messages.success(request, 'Successfully Edited')
                        return redirect('game_view', pk=review.game.pk)
                return render(request, 'review/view.html', context)

        else:
                messages.error(request, "Cannot edit: You are not the author.")
                return redirect('game_view', pk=review.game.pk)

def ReportReview(request, review_id):
        context = {}
        review = get_object_or_404(Review, pk=review_id)
        form = ReviewTicket(request.POST or None)
        context['review'] = review
        context['form'] = form
        if form.is_valid():
                form.moderation_target = review
                form.moderation_user = review.user
                form.instance.is_open = True
                cleaned_data = form.cleaned_data
                review.is_flagged = True
                review.moderation_message = form.instance.moderation_note
                review.save()
                form.save(cleaned_data)
                messages.success(request, 'Thank you for your feedback. A moderator will review your ticket and'
                                          'take appropriate action.')
                return redirect('game_view', pk=review.game.pk)
        return render(request, 'review/report.html', context)

def ProcessTickets(request, template_name='review/process_tickets'):
        context = {}
        flagged_reviews = ReviewTicket.objects.filter(ticket_open=True)
        context["flagged_reviews"] = flagged_reviews
        return render(request, template_name, context)





