from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import Post, Comment, PostLike
from .forms import PostForm, CommentForm
from django.contrib.auth import get_user_model
User = get_user_model()
#Logica - Regra de negocio
def post_list(request):
    posts = Post.objects.all()
    users = User.objects.all()
    return render(request, 'filme/post_list.html', {'posts': posts, 'users': users})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()

    liked = False
    if request.user.is_authenticated:
        likes_count = PostLike.objects.filter(post_id=pk,user=request.user).count()
        if likes_count > 0:
            liked = True


    percent = post.likes_count() / post.views * 100

    return render(request, 'filme/post_detail.html', {'post': post, 'liked': liked, 'percent': percent})

def author_perfil(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author)

    return render(request, 'filme/author_perfil.html', {'author': author, 'posts': posts})

#Se o usuário esta logado
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user

            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'filme/post_edit.html', {'form': form})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

#Se o usuário esta logado
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'filme/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'filme/post_draft_list.html', {'posts': posts})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'filme/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

'''def cadastrar_usuario(request):
    form = UsuarioForm()
    return render(request, "form.html", {'form':form})'''

@login_required
def post_like(request, pk):
    post_like, created = PostLike.objects.get_or_create(post_id=pk,user=request.user)

    return redirect('post_detail', pk=pk)

def post_list_blog(request):
    return render(request, 'blog/post_list.html', {})
