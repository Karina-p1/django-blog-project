"""
URL configuration for blogsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Importing the admin module from Django to enable the admin interface for managing the application
from django.urls import path, include # Importing the path and include functions from Django's urls module to define URL patterns and include URL configurations from other apps
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls), # Mapping the 'admin/' URL to the admin site, allowing access to the Django admin interface
    path('', include('blogapp.urls')), # Including the URL patterns defined in the blog app's urls.py file, which will handle the routing for the blog application
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adding static URL patterns to serve media files during development, using the MEDIA_URL and MEDIA_ROOT settings defined in the project's settings.py file