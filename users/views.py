from django.shortcuts import render
from django import forms

from merchant.models import Codes
# Create your views here.
class Login(forms.Form):
    Username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    Password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))

class Signup(forms.Form):
    f_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    l_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    Email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    Password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))


def user_dashboard(request):
    return render(request, "users/dashboard.html")

def index(request):
    context = {
        "codes": Codes.objects.all()
    }
    return render(request, "users/index.html", context)

def user_login(request):
    form = Login()
    context = {
        "form" : form
    }
    return render(request, "users/login.html", context)

def user_signup(request):
    form = Signup()
    context = {
        "form" : form
    }
    return render(request, "users/signup.html", context)