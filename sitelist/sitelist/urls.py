from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', RedirectView.as_view(url='polls/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Use static() to add url mapping to serve static files during development (only)
