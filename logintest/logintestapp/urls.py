from django.urls import path
from django.contrib.auth import views 
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login, name='login'),
]