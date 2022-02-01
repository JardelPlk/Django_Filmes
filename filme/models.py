from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

#Campos e variaveis do blog
class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #Caso alterar BD adicionar default='Some String', ex: models.CharField(max_length=200, default='Some String')
    titulo = models.CharField(max_length=200)
    ano = models.CharField(max_length=200)
    #aqui
    duracao = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    descricao = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.BigIntegerField(default=0)
    #likes = models.BigIntegerField(default=0)

#Pubicar na data e hora atual
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def likes_count(self):
        return PostLike.objects.filter(post=self).count()

    def __str__(self):
        return f'{self.titulo} ({self.autor})'

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('filme.Post', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.post.titulo, self.user)

class Comment(models.Model):
    post = models.ForeignKey('filme.Post', on_delete=models.CASCADE, related_name='comments')
    autor = models.CharField(max_length=200)
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.texto

def approved_comments(self):
    return self.comments.filter(approved_comment=True)
