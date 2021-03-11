from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.merchant_dashboard, name="merchantDashboard"),
    path('merchant/login/', views.merchant_login, name="merchantLogin"),
    path('merchant/events/', views.events, name="merchantGeneratedEvents"),
    path('merchant/welcome/', views.merchant_welcome, name="merchantWelcome"),
    path('merchant/scratch/form/', views.scratch_event, name="merchantScratch"),
    path('merchant/events/create', views.merchant_create_events, name="merchantEvents"),
]