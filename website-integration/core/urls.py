from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('video', main, name='main')
]