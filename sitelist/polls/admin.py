from importlib.resources import Resource

from django.contrib import admin
from polls.models import Owner, Meeting


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.register(Owner, OwnerAdmin)


@admin.register(Meeting)
class Meeting(admin.ModelAdmin):
    list_display = ('name_meeting', 'author', 'date_meeting')


class MeetingInstanceAdmin(admin.ModelAdmin):
    list_display = ('name_meeting', 'author', 'date_meeting', 'id')
    list_filter = ('status')


