from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ProjectForm, DiscotecaForm
from .models import Project
from .models import Discoteca 
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    form = UserCreationForm()
    return render(request, 'home.html', {
    })


def signup(request):
    if (request.method == 'GET'):
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrando usuaeuo+
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')

            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })

@login_required
def tasks(request):
    tasks = Project.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': ProjectForm
        })
    else:
        try:
            form = ProjectForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': ProjectForm,
                'error': 'Por favor provee un dato válido'
            })

def discotecas(request):
    discotecas = Discoteca.objects.all()
    return render(request, 'discotecas.html', {'discotecas': discotecas})

def create_discoteca(request):
    if request.method == 'GET':
        return render(request, 'create_discoteca.html', {
            'form': DiscotecaForm()
        })
    else:
        try:
            form = DiscotecaForm(request.POST)
            if form.is_valid():
                new_discoteca = form.save(commit=False)
                new_discoteca.user = request.user 
                new_discoteca.save()
                return redirect('discotecas') 
        except ValueError:
            return render(request, 'create_discoteca.html', {
                'form': DiscotecaForm(),
                'error': 'Por favor, provee datos válidos'
            })


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            next_url = request.GET.get('next', 'tasks') 
            return redirect(next_url)