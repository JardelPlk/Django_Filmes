from django.urls import path
from . import views

urlpatterns = [
    #Esta entre aspas para acessar direto da raiz
    path('', views.post_list_blog, name='post_list_blog'),
    path('post/<int:pk>/', views.post_detail_blog, name='post_detail_blog'),
    path('post/<int:pk>/edit/', views.post_edit_blog, name='post_edit_blog'),
    path('post/new/', views.post_new_blog, name='post_new_blog'),
    path('author/<username>/', views.author_perfil_blog, name='author_perfil_blog'),

    path('post/<int:pk>/publish/', views.post_publish_blog, name='post_publish_blog'),

    path('drafts/', views.post_draft_list_blog, name='post_draft_list_blog'),

    path('post/<int:pk>/remove/', views.post_remove_blog, name='post_remove_blog'),

    path('post/<int:pk>/comment/', views.add_comment_to_post_blog, name='add_comment_to_post_blog'),

    path('comment/<int:pk>/approve/', views.comment_approve_blog, name='comment_approve_blog'),
    path('comment/<int:pk>/remove/', views.comment_remove_blog, name='comment_remove_blog'),



]
