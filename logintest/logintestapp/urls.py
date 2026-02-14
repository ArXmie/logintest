from django.urls import path
from django.contrib.auth import views 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('personal/', views.personal, name='personal')
]