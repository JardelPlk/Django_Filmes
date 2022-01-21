from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'ano', 'duracao', 'genero', 'descricao', )#aqui

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('autor', 'texto',)
