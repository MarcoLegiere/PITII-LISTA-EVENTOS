from django.shortcuts import render
from . import admin
from .models import Owner, Meeting, User
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_meetings = Meeting.objects.all().count()

    # Available books
    num_users = User.objects.count()

    # The 'all()' is implied by default.
    num_authors = Owner.objects.count()

    #num_visits = request.session.get('num_visits', 0)
    #request.session['num_visits'] = num_visits + 1

    context = {
        'num_meetings': num_meetings,
        'num_users': num_users,
        'num_authors': num_authors,
        #'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class MeetingListView(generic.ListView):
    model = Meeting


class MeetingDetailView(generic.DetailView):
    model = Meeting

from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Meeting
    template_name ='catalog/meeting_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Meeting.objects.filter(borrower=self.request.user).filter(status__exact='p' or 'f').order_by('due_back')


