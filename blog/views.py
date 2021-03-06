from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth import get_user_model
from users.forms import CustomUserChangeForm

User = get_user_model()

#Logica - Regra de negocio
def post_list_blog(request):
    posts = Post.objects.all()
    users = User.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'users': users})

def post_detail_blog(request, pk):
    #try:
    #    post = Post.objects.get(pk=pk)
    #except Post.DoesNotExist:
    #    raise Http404('Post missing =/')

    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})

def author_perfil_blog(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author)

    return render(request, 'blog/author_perfil.html', {'author': author, 'posts': posts})

#Se o usuário esta logado
@login_required
def post_new_blog(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('post_detail_blog', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_publish_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail_blog', pk=pk)

#Se o usuário esta logado
@login_required
def post_edit_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_blog', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list_blog(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_remove_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail_blog', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve_blog(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail_blog', pk=comment.post.pk)

@login_required
def comment_remove_blog(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail_blog', pk=comment.post.pk)
