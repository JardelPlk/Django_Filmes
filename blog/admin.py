from django.contrib import admin
from .models import Post, Comment

#Ligar a pagina
admin.site.register(Post)
admin.site.register(Comment)
