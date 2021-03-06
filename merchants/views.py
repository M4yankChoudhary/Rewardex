from django.shortcuts import render
from django import forms

# Create your views here.
class Login(forms.Form):
    Username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    Password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))


def merchant_dashboard(request):
    return render(request, "merchants/dashboard.html")

def merchant_events(request):
    return render(request, "merchants/events.html")

def merchant_welcome(request):
    return render(request, "merchants/welcome.html")   

def merchant_login(request):
    form = Login()
    context = {
        "form" : form
    }
    return render(request, "merchants/login.html", context)