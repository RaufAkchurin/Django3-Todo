
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home(request):
    return render(request, 'todoo/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todoo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return redirect('current')
            except IntegrityError:
                return render(request, 'todoo/signupuser.html', {'form': UserCreationForm(),
                                                                'error':'Пользователь с таким именем уже существует'})
        else:
            return render(request, 'todoo/signupuser.html', {'form': UserCreationForm(),
                                                             'error': ' Введённые пароли не совпадают'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todoo/signupuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todoo/signupuser.html', {'form': AuthenticationForm(),
                                                             'error': 'Неверный логин или пароль'})
        else:
            login(request, user)
            return redirect('current')


def current(request):
    return render(request, 'todoo/current.html')

