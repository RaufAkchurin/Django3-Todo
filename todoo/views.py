
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


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


@login_required()
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todoo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todoo/loginuser.html', {'form': AuthenticationForm(),
                                                             'error': 'Неверный логин или пароль'})
        else:
            login(request, user)
            return redirect('current')


@login_required()
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todoo/createtodo.html', {'form': TodoForm})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('current')
        except ValueError:
            return render(request, 'todoo/createtodo.html', {'form': TodoForm, 'error': 'Неверные данные'})


@login_required()
def current(request):
    todos = Todo.objects.filter(user=request.user, complete__isnull=True)
    return render(request, 'todoo/current.html', {'todos': todos})


@login_required()
def completed(request):
    todos = Todo.objects.filter(user=request.user, complete__isnull=False)
    return render(request, 'todoo/completed.html', {'todos': todos})


@login_required()
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todoo/viewtodo.html', {'todo': todo, 'form': form})
    else:
        form = TodoForm(request.POST, instance=todo)
        form.save()
        return redirect('current')


@login_required()
def completetodo(request, todo_pk):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
        todo.complete = timezone.now()
        todo.save()
        return redirect('current')


@login_required()
def deletetodo(request, todo_pk):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
        todo.delete()
        return redirect('current')
