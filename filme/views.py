from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import Post, Comment, PostLike
from .forms import PostForm, CommentForm
from django.contrib.auth import get_user_model
from users.forms import CustomUserChangeForm
from django.contrib import messages

User = get_user_model()
#Logica - Regra de negocio
def post_list(request):
    posts = Post.objects.all()
    users = User.objects.all()
    if len(posts) == 0:
        messages.info(request, 'Não existe nenhum filme!')
    else:
        messages.success(request, 'Filmes listados com sucesso.')
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
            messages.success(request, 'Post salvo com sucesso!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'filme/post_edit.html', {'form': form})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    messages.success(request, 'Filme publicado com sucesso.')
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
        #messages.info(request, 'Post não encontrado.')
    return render(request, 'filme/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    if len(posts) == 0:
        messages.info(request, 'Não existe nenhum filme.')
    else:
        messages.info(request, 'Filmes não publicados.')
    return render(request, 'filme/post_draft_list.html', {'posts': posts})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    #messages.success(request, 'Post deletado com sucesso.')
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
    messages.info(request, 'Comentário aprovado.')
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    messages.info(request, 'Comentário removido.')
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def post_like(request, pk):
    post_like, created = PostLike.objects.get_or_create(post_id=pk,user=request.user)

    return redirect('post_detail', pk=pk)

def post_list_blog(request):
    return render(request, 'blog/post_list.html', {})

@login_required
def user_list(request):
    UserModel = get_user_model()
    users = UserModel.objects.all().order_by('birth_date')
    messages.success(request, 'Usuários listados com sucesso.')
    return render(request, 'filme/user_list.html', {'users': users})

@login_required
def user_remove(request, pk):
    UserModel = get_user_model()
    user = get_object_or_404(UserModel, pk=pk)
    user.delete()

    return redirect('user_list')

@login_required
def user_edit(request, pk):
    UserModel = get_user_model()
    user = get_object_or_404(UserModel, pk=pk)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, 'filme/user_edit.html', {'form': form})
