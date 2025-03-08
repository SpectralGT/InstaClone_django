from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

# Create your views here.


def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.Info(request, "email already exist")
                return redirect("signup.html")
        else:
            messages.Info(request, "Password not matching")
            return redirect("signup.html")
    return render(request, "index.html")


def signup(request):
    return render(request, "signup.html")
