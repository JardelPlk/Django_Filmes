from django.urls import path, include
from django.contrib import admin

from django.contrib.auth import views

#Caminhos do site
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('filme.urls')),#O que vem depois de blog são as urls la na pasta do blog
]
