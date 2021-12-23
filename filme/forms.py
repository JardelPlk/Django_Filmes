from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'text2', )#aqui

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

'''class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "email", "sexo"]'''