from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate

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
    if request.method == "POST":
        login_form = Login(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['Username']
            password = login_form.cleaned_data['Password']
            # user = authenticate(username=username, password=password)
            # user = User.objects.all()
            # group = Group.objects.get(name="merchants")
            # user_in_group = Group.objects.all()
            check_user = User.objects.filter(groups__name="merchants")
            
            if check_user is not None:
                for i in check_user:
                    i = str(i)
                    if username == i:
                        user = authenticate(username=username, password=password)
                        if user is not None:
                            return HttpResponse("Logged in as merchant")
                        return HttpResponse("Error")
                return HttpResponse("Not a merchant")
            return HttpResponse("Login failed")
    context = {
        "form" : form
    }
    return render(request, "merchants/login.html", context)


class Scratchgame(forms.Form):
    Offerpercnt = forms.IntegerField(label="Offer percent", widget=forms.TextInput(attrs={'class' : 'form-control text-center'}))
    minorderplace = forms.IntegerField(label="Minimum order place", widget=forms.TextInput(attrs={'class' : 'form-control text-center'}))
    validdays = forms.IntegerField(label="Valid days", widget=forms.TextInput(attrs={'class' : 'form-control text-center'}))

def scratch_event(request):
    formscratch = Scratchgame()
    context = {
    "formscratch" : formscratch
    }
    return render(request, "merchants/scratchform.html", context)