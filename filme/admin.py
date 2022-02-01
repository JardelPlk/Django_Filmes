from django.contrib import admin
from .models import Post, Comment, PostLike

#Ligar a pagina
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostLike)
