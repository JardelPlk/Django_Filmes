from django.urls import path
from . import views

urlpatterns = [
    #Esta entre aspas para acessar direto da raiz
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('author/<username>/', views.author_perfil, name='author_perfil'),

    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),

    path('drafts/', views.post_draft_list, name='post_draft_list'),

    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/like/', views.post_like, name='post_like'),

    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('', views.post_list_blog, name='post_list_blog'),

    #CustomUsers
    path('users/', views.user_list, name='user_list'),
    path('user/<pk>/edit/', views.user_edit, name='user_edit'),
    path('user/<pk>/remove/', views.user_remove, name='user_remove'),

]
