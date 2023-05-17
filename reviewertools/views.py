from datetime import time, datetime

from django.core.mail import send_mail

from accounts.mixins import StaffRequiredMixin
from reviewertools.models import Review, ReviewTicket
from accounts.models import CustomUser
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, ReviewTicketForm, TicketResolutionForm
from groupproject.forms import Game
from django.contrib import messages
from django.conf import settings

def ReviewIndexTest(request):
        context = {}
        return render(request, 'review/reviewindex.html', context)

def CreateReview(request, game_id):
        if not request.user.is_authenticated:
                messages.error(request, "Please log in to access this page.")
                return redirect('login')
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
                return redirect('game_view', pk=game.pk)
        else:
                print('failure')

        return render(request, 'review/view.html', context)


def UpdateReview(request, review_id):
        if not request.user.is_authenticated:
                messages.error(request, "Please log in to access this page.")
                return redirect('login')
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
        form = ReviewTicketForm(request.POST or None, request.FILES or None)
        context['review'] = review
        context['form'] = form
        print(review.user.username)
        print(review.game.title)
        if form.is_valid():
                form.instance.moderation_target = review
                form.instance.moderation_user = review.user
                form.instance.ticket_open = True
                cleaned_data = form.cleaned_data
                review.is_flagged = True
                review.moderation_message = form.instance.moderation_note
                review.save()
                form.save(cleaned_data)
                messages.success(request, 'Thank you for your feedback. A moderator will review your ticket and'
                                          'take appropriate action.')
                return redirect('game_view', pk=review.game.pk)
        return render(request, 'review/report.html', context)


def ListOpenTickets(request, template_name='review/process_tickets.html'):
        result = StaffRequiredMixin().dispatch(request)
        if not result == None:
                return result
        context = {}
        flagged_reviews = ReviewTicket.objects.filter(ticket_open=True)
        context["flagged_reviews"] = flagged_reviews
        return render(request, template_name, context)

def ProcessIndividualTicket(request, ticket_id, template_name='review/ticket_view.html'):
        result = StaffRequiredMixin().dispatch(request)
        if not result == None:
                return result
        context = {}
        ticket = get_object_or_404(ReviewTicket, pk=ticket_id)
        user = CustomUser.objects.filter(pk=ticket.moderation_user.pk)[0]
        form = TicketResolutionForm(request.POST or None, initial={'outcome': False, 'ban_user': False})
        context= {
                'review':ticket.moderation_target,
                'ticket':ticket,
                'form':form,
                'user':user,
        }
        if form.is_valid():
                if form.cleaned_data['outcome'] == True:
                        user.moderation_message = form.cleaned_data['message_to_creator']
                        # if form.data['ban_user']:
                        if request.POST.get('ban_user', False):
                                banned = "Unfortunately, we have decided to remove your ability to post reviews until further notice."
                                user.is_onprobation = True
                        else:
                                banned = "While we have removed your review, we hope you continue to add your input and look" \
                                         "forward to your future contributions."
                        subject = f"{user.first_name}, a review you posted has been removed."
                        body = f"Hello {user.first_name}. After reviewing a complaint against a review you" \
                               f"posted on our site, the staff has determined that due to its inappropriate" \
                               f"that it should be removed. {banned} If you have any further questions, don't ask them."
                        # Mailing disabled since I have reached a set limit.
                        # send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [user.email])
                else:
                        context['review'].is_flagged = False
                        context['review'].save()
                ticket.change_status()
                ticket.save()
                user.save()
                messages.success(request, 'Ticket has been reviewed and closed.')
                return redirect('process_tickets')
        return render(request, template_name, context)








