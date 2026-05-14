from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .forms import RegisterForm, PostForm, CommentForm, ProfileForm
from .models import Post, Profile, Category


def home(request):
    query       = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '')
    posts       = Post.objects.all().order_by('-created_at')
    categories  = Category.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    if category_id:
        posts = posts.filter(category__id=category_id)

    selected_category = None
    if category_id:
        try:
            selected_category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            pass

    return render(request, 'blog/home.html', {
        'posts': posts,
        'query': query,
        'categories': categories,
        'selected_category': selected_category,
    })


def post_detail(request, id):
    post         = get_object_or_404(Post, id=id)
    comment_form = CommentForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment      = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', id=post.id)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comment_form': comment_form,
    })


@login_required
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post        = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('home')
    return render(request, 'blog/create_post.html', {'form': form})


@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        messages.error(request, 'You are not allowed to edit this post.')
        return redirect('home')
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', id=post.id)
    return render(request, 'blog/update_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        messages.error(request, 'You are not allowed to delete this post.')
        return redirect('home')
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('home')
    return render(request, 'blog/delete_post.html', {'post': post})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You can now log in.')
            return redirect('login')
    return render(request, 'blog/register.html', {'form': form})


@login_required
@require_POST
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'total_likes': post.total_likes()})


def profile_view(request, username):
    profile_user    = get_object_or_404(User, username=username)
    profile, _      = Profile.objects.get_or_create(user=profile_user)
    posts           = Post.objects.filter(author=profile_user).order_by('-created_at')
    return render(request, 'blog/profile.html', {
        'profile_user': profile_user,
        'profile': profile,
        'posts': posts,
    })


@login_required
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    form       = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect('profile', username=request.user.username)
    return render(request, 'blog/edit_profile.html', {'form': form})