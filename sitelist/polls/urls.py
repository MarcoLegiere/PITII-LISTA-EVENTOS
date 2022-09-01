from django.urls import path, include
from polls import views


urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns = [
    path('', views.index, name='index'),
    path('meeting/', views.MeetingListView.as_view(), name='meeting'),
    path('meeting/<int:pk>', views.MeetingDetailView.as_view(), name='meeting_detail'),
]
