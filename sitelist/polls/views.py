from django.shortcuts import render
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

    context = {
        'num_meetings': num_meetings,
        'num_users': num_users,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class MeetingListView(generic.ListView):
    model = Meeting


class MeetingDetailView(generic.DetailView):
    model = Meeting


