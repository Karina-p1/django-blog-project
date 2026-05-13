from django import forms  # Importing the forms module from Django, which provides a way to create and handle forms in a Django application
from .models import Post, Comment, Profile # Importing the Post and Comment models from the current app's models.py file, which will be used to create forms for creating and editing posts and comments
from django.contrib.auth.forms import UserCreationForm # Importing the UserCreationForm from Django's auth forms, which provides a built-in form for user registration, allowing users to create an account with a username and password
from django.contrib.auth.models import User # Importing the User model from Django's auth models, which represents a user in the application and will be used to create a registration form for new users

# This code defines three form classes for a Django application: RegisterForm, PostForm, and CommentForm.
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']  # image field added
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']