from django.urls import path, include
from django.contrib import admin
from refugio import views


urlpatterns = [    
    path('',include('refugio.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('',include('social.apps.django_app.urls', namespace='social')),
] 
