from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.shortcuts import render
from django import forms
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
class Login(forms.Form):
    Username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control text-center col-md-8 col-lg-8'}))
    Password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control text-center col-md-8 col-lg-8'}))


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
    validupto = forms.DateField(label="Valid upto", initial = datetime.date.today, widget=forms.DateInput(attrs={'class' : 'form-control text-center', 'type': 'date'}))

def scratch_event(request):
    formscratch = Scratchgame()

    if request.method == "POST":
        form = Scratchgame(request.POST)
        if form.is_valid():
            offer_upto = form.cleaned_data["Offerpercnt"]
            min_order = form.cleaned_data["minorderplace"]
            valid_upto = form.cleaned_data["validupto"]

            merchant = MerchantName.objects.all()
            get_name = None
            for i in merchant:
                print(i)
                get_name = i

            code = Codes(code="ueeu67", offer=offer_upto, minimum_value=min_order, date=valid_upto, store_owner=get_name)
            code.save()

            return HttpResponseRedirect(reverse('merchantEvents'))



    context = {
    "formscratch" : formscratch
    }
    return render(request, "merchants/scratchform.html", context)