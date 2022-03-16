from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'todo/home.html')


def singupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/singupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                error = 'That username has already been taken. Please choose a new username'
                return render(request, 'todo/singupuser.html', {'form': UserCreationForm(),
                                                                'error': error})
        else:
            error = 'Password did not match'
            return render(request, 'todo/singupuser.html', {'form': UserCreationForm(),
                                                            'error': error})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username= request.POST['username'], password= request.POST['password'])
        if user is None:
            error = 'Username and password did not match'
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(),
                                                           'error': error})
        else:
            login(request, user)
            return redirect('currenttodos')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def currenttodos(request):
    return render(request, 'todo/currenttodos.html')