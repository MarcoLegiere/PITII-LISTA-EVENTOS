from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


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