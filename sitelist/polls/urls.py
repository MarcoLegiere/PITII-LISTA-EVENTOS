from django.urls import path, include
from polls import views


urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns = [
    path('', views.index, name='index'),
    path('meeting/', views.MeetingListView.as_view(), name='meeting'),
    path('meeting/<str:pk>', views.MeetingDetailView.as_view(), name='meetingDetail'),
    path('mymeetings/<str:pk>', views.MeetingDetailView.as_view(), name='my-meetingsDetail'),
]

urlpatterns += [
    path('mymeetings/create/', views.MeetingCreate.as_view(), name='mymeeting_create'),
    path('mymeetings/<str:pk>/update/', views.MeetingUpdate.as_view(), name='mymeeting_update'),
    path('meetings/<str:pk>/delete/', views.MeetingDelete.as_view(), name='mymeeting_delete'),
]

urlpatterns +=[
    path('meeting/<str:pk>/user/', views.UserCreate.as_view(), name='user'),
]