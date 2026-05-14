from django.db import models # Importing the models module from Django to create database models
from django.contrib.auth.models import User # Importing the User model from Django's built-in authentication system to associate posts and comments with users
from django.utils import timezone # Importing the timezone utility from Django to handle date and time fields
from django.db.models.signals import post_save
from django.dispatch import receiver

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
 
    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name_plural = "Categories"

# post model to represent a blog post in the database
class Post(models.Model):
    title = models.CharField(max_length=200) 
    content = models.TextField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Optional image field for the post
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)  
    category   = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    def total_likes(self):
        return self.likes.count()

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
    
# Profile model
class Profile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    bio    = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    Profile.objects.get_or_create(user=instance)
    instance.profile.save()
