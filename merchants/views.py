from django.shortcuts import render

# Create your views here.

def merchant_index(request):
    return render(request, "merchants/index.html")