from django.db import models # Importing the models module from Django to create database models
from django.contrib.auth.models import User # Importing the User model from Django's built-in authentication system to associate posts and comments with users
from django.utils import timezone # Importing the timezone utility from Django to handle date and time fields

# post model to represent a blog post in the database
class Post(models.Model):
    title = models.CharField(max_length=200) 
    content = models.TextField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Optional image field for the post

    def __str__(self):
        return self.title

# comment model to represent comments on blog posts in the database 
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:30] # Return the first 30 characters of the comment as its string representation