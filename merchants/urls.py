from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.merchant_dashboard, name="merchantDashboard"),
    path('merchant/login/', views.merchant_login, name="merchantLogin"),
    path('merchant/events/', views.merchant_events, name="merchantEvents"),
]