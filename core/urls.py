from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import *

urlpatterns = [
    path('',about.home,name='home'),
    path('user/signup', user.signup, name='signup'),
    path('user/login', user.user_login, name='login'),
    path('user/signup_confirm/<int:id>', user.signup_confirm, name='signup_confirm'),
    path('user/logout', user.user_logout, name='logout'),
]