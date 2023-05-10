from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist

def register(request):
    if (request.user.is_authenticated):
        return redirect('home:index')
    
    if (request.method == "POST"):
        __email      = request.POST["email"]
        __username   = request.POST["username"]
        __password_1 = request.POST["password"]
        __password_2 = request.POST["password2"]

        if __password_1 != __password_2:
            messages.info(request, "Passwords don't match")
            return redirect('account:register')

        if User.objects.filter(username = __username).exists():
            messages.info(request, "User with username \"" + __username + "\" already exists")
            return redirect('account:register')
        elif User.objects.filter(email = __email).exists():
            messages.info(request, "Email \"" + __email + "\" is already being used")
            return redirect('account:register')

        user = User.objects.create_user(email = __email, username = __username, password = __password_1)
        user.save()

        messages.info(request, "You were successfully registered")
        return redirect('account:login')
    else:
        return render(request, 'account/register.html')

def login(request):
    if (request.user.is_authenticated):
        return redirect('home:index')
    
    if (request.method == "POST"):

        __username = request.POST["username"]
        __password = request.POST["password"]

        user = auth.authenticate(username = __username, password = __password)

        if user is None:
            messages.info(request, "Invalid username or password")
            return redirect('account:login')
        else:
            auth.login(request, user)
            return redirect('home:index')
    else:
        return render(request, 'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home:index')