from django.urls import path, include
from polls import views


urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns = [
    path('', views.index, name='index'),
    path('meeting/', views.MeetingListView.as_view(), name='meeting'),
    path('meeting/<str:pk>', views.MeetingDetailView.as_view(), name='meetingDetail'),
]
