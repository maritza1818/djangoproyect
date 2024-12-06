from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ProjectForm, DiscotecaForm
from .models import Project
from .models import Discoteca
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages


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


def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Project, pk=task_id, user=request.user)
        form = ProjectForm(instance=task)
        return render(request, 'tasks_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Project, pk=task_id, user=request.user)
            form = ProjectForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'tasks_detail.html', {'task': task, 'form': form,
            'error': 'Por favor, provee datos válidos'
            })
def complete_task(request, task_id):
    task = get_object_or_404(Project, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        messages.success(request, '¡La tarea ha sido marcada como completada!')
        return redirect('tasks') 
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


def discoteca_detail(request, discoteca_id):
    if request.method == 'GET':
        discoteca = get_object_or_404(Discoteca, pk=discoteca_id, user=request.user)
        form = DiscotecaForm(instance=discoteca)
        return render(request, 'discoteca_detail.html', {'discoteca': discoteca, 'form': form})
    else:
        try:
            discoteca = get_object_or_404(Discoteca, pk=discoteca_id, user=request.user)
            form = DiscotecaForm(request.POST, instance=discoteca)
            form.save()
            return redirect('discotecas')
        except ValueError:
            return render(request, 'discoteca_detail.html', {'discoteca': discoteca, 'form': form,
            'error': "Error de actualizar la tarea"})
def complete_discoteca(request, discoteca_id):
    discoteca = get_object_or_404(Discoteca, pk=discoteca_id, user=request.user)
    if request.method == 'POST':
        discoteca.datecompleted = timezone.now()
        discoteca.save()
        messages.success(request, '¡La discoteca ha sido marcada como completada!')

        return redirect('discotecas') 

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
