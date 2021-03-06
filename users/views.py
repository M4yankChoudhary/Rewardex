from django.shortcuts import render

# Create your views here.

def user_index(request):
    return render(request, "users/index.html")