from django.contrib import admin
from polls.models import Owner, Meeting, User

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Owner, OwnerAdmin)

@admin.register(Meeting)
class Meeting(admin.ModelAdmin):
    list_display = ('name_meeting', 'author', 'date_meeting')

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('meeting', 'name', 'matricula', 'setor', 'cargo', 'email')
    fields = ['name', 'email', ('cago', 'setor')]

