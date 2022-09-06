from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import include
from django.urls import path
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='polls/', permanent=True)),
]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('mymeetings/', views.LoanedMeetingsByUserListView.as_view(), name='my-meetings'),
    path('mymeetings/<str:pk>', views.LoanedMeetingsByUserDetailView.as_view(), name='my-meetingsDetail'),
]

urlpatterns += [
    path('meeting/create/', views.MeetingCreate.as_view(), name='meeting-create'),
    path('meeting/<str:pk>/update/', views.MeetingUpdate.as_view(), name='meeting-update'),
    path('meeting/<str:pk>/delete/', views.MeetingDelete.as_view(), name='meeting-delete'),
]

