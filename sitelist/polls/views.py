from django.shortcuts import render
from pyexpat.errors import messages

from . import forms

from .models import Owner, Meeting
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from polls.models import Meeting


def index(request):

    return render(request, 'index.html')

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
    fields = ['name_meeting', 'date_meeting', 'link', 'local', 'public', 'status', 'descricao']
    initial = {'status': 'f'}
    success_url = reverse_lazy('my-meetings')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MeetingUpdate(UpdateView):
    model = Meeting
    fields = ['name_meeting', 'date_meeting', 'link', 'local', 'public', 'status', 'descricao']
    success_url = reverse_lazy('my-meetings')

class MeetingDelete(DeleteView):
    model = Meeting
    success_url = reverse_lazy('my-meetings')





