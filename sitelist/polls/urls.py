from django.urls import path, include
from polls import views


urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('polls/', include('polls.urls')),
]
