from importlib.resources import Resource

from django.shortcuts import render
from . import admin
from .models import Owner, Meeting, Funcionario
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from polls.models import Meeting


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_meetings = Meeting.objects.all().count()

    # Available books
    num_users = Funcionario.objects.count()

    context = {
        'num_meetings': num_meetings,
        'num_users': num_users,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class MeetingListView(generic.ListView):
    model = Meeting
    template_name = 'polls/meeting_list.html'

    def get_queryset(self):
        return Meeting.objects.filter().filter(status__exact='p').order_by('public')


class MeetingDetailView(generic.DetailView):
    model = Meeting


class LoanedMeetingsByUserListView(LoginRequiredMixin, generic.ListView):
    model = Meeting
    template_name = 'polls/meeting_list_borrowed_user.html'

    def get_queryset(self):
        status = ['p', 'f']
        return Meeting.objects.filter(author=self.request.user).filter(status__in=status).order_by('date_meeting')


class LoanedMeetingsByUserDetailView(LoginRequiredMixin, generic.DetailView):
    """Generic class-based view listing books on loan to current user."""
    model = Meeting
    template_name = 'polls/meeting_detail_borrowed_user.html'


class MeetingCreate(CreateView):
    model = Meeting
    fields = ['name_meeting', 'date_meeting', 'link', 'local', 'public', 'status']
    initial = {'status': 'f'}
    success_url = reverse_lazy('my-meetings')

    def form_valid(self, form):
        form.instance.author = self.request.user
        url = super().form_valid(form)
        return url


class MeetingUpdate(UpdateView):
    model = Meeting
    fields = ['name_meeting', 'date_meeting', 'link', 'local', 'public', 'status']
    success_url = reverse_lazy('my-meetings')


class MeetingDelete(DeleteView):
    model = Meeting
    success_url = reverse_lazy('my-meetings')


class FuncionarioCreate(CreateView):
    model = Funcionario
    success_url = reverse_lazy('meeting')
    fields = [
        'nome',
        'matricula',
        'email',
        'setor',
        'cargo'
    ]

    def form_valid(self, form):
        form.instance.meetingconfirm = self.request.meeting('pk')
        url = super().form_valid(form)
        return url
