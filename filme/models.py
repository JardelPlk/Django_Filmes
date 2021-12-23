from django.db import models
from django.conf import settings
from django.utils import timezone

'''class Usuario(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]

    nome = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
'''

#Campos e variaveis do blog
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    #aqui
    text2 = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

#Pubicar na data e hora atual
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.title} ({self.author})'

class Comment(models.Model):
    post = models.ForeignKey('filme.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

def approved_comments(self):
    return self.comments.filter(approved_comment=True)