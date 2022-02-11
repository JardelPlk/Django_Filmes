from django.urls import path, include
from django.contrib import admin

from django.contrib.auth import views

#Caminhos do site
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('filme.urls')),#O que vem depois de filme são as urls la na pasta do filme
    path('blog/', include('blog.urls')),
]
