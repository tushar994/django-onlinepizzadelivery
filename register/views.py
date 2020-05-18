from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'register.html')
    else:
        return redirect('/shop/')

def login_r(request):
    context = {
        'to_go_to' : 'login_result',
        'text' : 'login',
    }
    return render(request, 'sign_up.html', context)

def register(request):
    context = {
        'to_go_to' : 'register_result',
        'text' : 'register',
    }
    return render(request, "sign_up.html", context)

def register_result(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        context = {
            'to_go_to' : 'register_result',
            'text' : 'register',
            'error_message' : 'Username taken'
        }
        return render(request, "sign_up.html", context)
    else:
        user = User.objects.create_user(username, email, password)
        user.save()
        login(request,user)
        # context = {
        #     'to_go_to' : 'register_result',
        #     'text' : 'register',
        #     'error_message' : 'registered'
        # }
        return redirect('/shop/')

def login_result(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # context = {
        #     'to_go_to' : 'login_result',
        #     'text' : 'login',
        #     'error_message' : 'logged in '
        # }
        return redirect('/shop/')
    else:
        context = {
            'to_go_to' : 'login_result',
            'text' : 'login',
            'error_message' : 'no such user'
        }
        return render(request, "sign_up.html", context)

def logout_bro(request):
    logout(request)
    return render(request, 'register.html')
