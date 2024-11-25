from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cal/', include('cal.urls')),  # Your app's URLs
    path('', RedirectView.as_view(url='cal/calculate/', permanent=False)),  # Redirect root to calculate
]