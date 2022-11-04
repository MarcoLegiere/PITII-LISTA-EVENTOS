from django.urls import path, include
from polls import views


urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('meeting/', views.MeetingListView.as_view(), name='meeting'),
    path('meeting/<uuid:pk>', views.MeetingDetailView.as_view(), name='meetingDetail'),
    path('mymeetings/<uuid:pk>', views.MeetingDetailView.as_view(), name='my-meetingsDetail'),
]

urlpatterns += [
    path('mymeetings/create/', views.MeetingCreate.as_view(), name='mymeeting_create'),
    path('mymeetings/<uuid:pk>/update/', views.MeetingUpdate.as_view(), name='mymeeting_update'),
    path('meetings/<uuid:pk>/delete/', views.MeetingDelete.as_view(), name='mymeeting_delete'),
]
