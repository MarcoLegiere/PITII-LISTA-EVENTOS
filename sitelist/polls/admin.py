from django.contrib import admin
from polls.models import Owner, Meeting, User

admin.site.register(Owner)
admin.site.register(Meeting)
admin.site.register(User)