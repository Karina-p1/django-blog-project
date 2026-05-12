from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comment_form = CommentForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', id=post.id)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comment_form': comment_form
    })


@login_required
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Include request.FILES to handle image uploads
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('home')
    return render(request, 'blog/create_post.html', {'form': form})


@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)

    # Only the author can edit
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

    # Only the author can delete
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