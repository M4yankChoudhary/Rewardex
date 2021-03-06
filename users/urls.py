from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.user_dashboard, name="userIndex"),
    path('login/', views.user_login, name="userLogin"),
    path('signup/', views.user_signup, name="userSignup"),
]