from django.urls import path

from . import views

urlpatterns = [
    path('sigup/', views.SigUp.as_view(), name='sigup'),
]
