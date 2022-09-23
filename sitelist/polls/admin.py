from importlib.resources import Resource

from django.contrib import admin
from polls.models import Owner, Meeting, Funcionario


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.register(Owner, OwnerAdmin)


@admin.register(Meeting)
class Meeting(admin.ModelAdmin):
    list_display = ('name_meeting', 'author', 'date_meeting')


class MeetingInstanceAdmin(admin.ModelAdmin):
    list_display = ('name_meeting', 'author', 'date_meeting', 'id')
    list_filter = ('status')


@admin.register(Funcionario)
class Funcionario(admin.ModelAdmin):
    list_display = ('meeting','nome', 'matricula', 'setor', 'cargo', 'email', 'meeting_id')
    fields = ['meeting', 'nome', 'email', ('cargo', 'setor')]

    def form_valid(self, form):
        form.instance.meeting = self.request.meeting
        return super().form_valid(form)
