from django.contrib import admin # Importing the admin module from Django to register models for the admin interface
from .models import Post, Comment, Profile # Importing the Post and Comment models from the current app's models.py file to register them with the admin site

admin.site.register(Post) # Registering the Post model with the admin site to make it manageable through the Django admin interface
admin.site.register(Comment) # Registering the Comment model with the admin site to make it manageable through the Django admin interface
admin.site.register(Profile) # Registering the Profile model with the admin site to make it manageable through the Django admin interface