from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'ano', 'duracao', 'genero', 'descricao', )#aqui

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Criar', css_class='btn-lg save'))

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('autor', 'texto',)
