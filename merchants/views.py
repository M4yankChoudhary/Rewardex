from django.shortcuts import render
from django import forms

# Create your views here.
class Login(forms.Form):
    Username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    Password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))

class Scrachgame(forms.Form):
    Offerpercnt = forms.IntegerField(label="Offer percent", widget=forms.TextInput(attrs={'class' : 'form-control text-center'}))
    minorderplace = forms.IntegerField(label="Minimum order place", widget=forms.TextInput(attrs={'class' : 'form-control text-center'}))
    validdays = forms.IntegerField(label="Valid days", widget=forms.TextInput(attrs={'class' : 'form-control text-center'}))

class Spingame(forms.Form):
    Offerpercnt = forms.IntegerField(label="Offer percent", widget=forms.TextInput(attrs={'class' : 'form-control text-center'}))
    minorderplace = forms.IntegerField(label="Minimum order place", widget=forms.TextInput(attrs={'class' : 'form-control text-center'}))
    validdays = forms.IntegerField(label="Valid days", widget=forms.TextInput(attrs={'class' : 'form-control text-center'}))

class QRgame(forms.Form):
    Offerpercnt = forms.IntegerField(label="Offer percent", widget=forms.TextInput(attrs={'class' : 'form-control text-center'}))
    minorderplace = forms.IntegerField(label="Minimum order place", widget=forms.TextInput(attrs={'class' : 'form-control text-center'}))
    validdays = forms.IntegerField(label="Valid days", widget=forms.TextInput(attrs={'class' : 'form-control text-center'}))


def merchant_dashboard(request):
    return render(request, "merchants/dashboard.html")

def merchant_events(request):
    return render(request, "merchants/events.html")

def merchant_login(request):
    form = Login()
    context = {
        "form" : form
    }
    return render(request, "merchants/login.html", context)

def spin_event(request):
    formspin = Spingame()
    context = {
        "formspin" : formspin
    }
    return render(request, "merchants/spinform.html", context)

def qrcode_event(request):
    formQR = QRgame()
    context = {
    "formQR" : formQR
    }
    return render(request, "merchants/qrform.html", context)

def scrach_event(request):
    formscrach = Scrachgame()
    context = {
    "formscrach" : formscrach
    }
    return render(request, "merchants/scrachform.html", context)

   



        

