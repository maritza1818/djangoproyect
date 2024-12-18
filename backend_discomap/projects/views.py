import json
import jwt
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ProjectForm, DiscotecaForm
from .models import Project, Discoteca
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.conf import settings


@api_view(['POST'])
def signin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token = jwt.encode({'username': username}, 'secret_key', algorithm='HS256')
            return JsonResponse({'token': token})
        else:
            return JsonResponse({'error': 'Username or password is incorrect'}, status=400)

@csrf_exempt
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password1 = data.get('password1')
            password2 = data.get('password2')
            
            print(f"Username: {username}, Password1: {password1}, Password2: {password2}")  # Verificar los datos recibidos
            
            if password1 != password2:
                return JsonResponse({'error': 'Passwords do not match'}, status=400)
            
            if not username or not password1:
                return JsonResponse({"error": "Username and password are required"}, status=400)
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists"}, status=400)
            
            user = User.objects.create_user(username=username)  # Crear el usuario
            user.set_password(password1)  # Encriptar la contraseña
            user.save()
            
            login(request, user)
            token = jwt.encode({'username': username}, 'secret_key', algorithm='HS256')
            return JsonResponse({'token': token}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return JsonResponse({'error': str(e)}, status=500)




@api_view(['POST'])
def signout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'User logged out successfully'})

@csrf_exempt
def discotecas_json(request):
    if request.method == 'GET':
        discotecas = Discoteca.objects.all()  
        data = []
        for discoteca in discotecas:
            imagen_url = discoteca.imagen.url if discoteca.imagen else None
            data.append({
                'id': discoteca.id,
                'nombre': discoteca.nombre,
                'direccion': discoteca.direccion,
                'telefono': discoteca.telefono,
                'descripcion': discoteca.descripcion,
                'fecha_creacion': discoteca.created_at.strftime('%Y-%m-%d'),  
                'horario_apertura': discoteca.horario_apertura.strftime('%H:%M:%S'),
                'horario_cierre': discoteca.horario_cierre.strftime('%H:%M:%S'),
                'aforo_maximo': discoteca.aforo_maximo,
                'stock_bebidas': discoteca.stock_bebidas,
                'calificacion': float(discoteca.calificacion),
                'imagen': imagen_url,
                'redes_sociales': json.loads(discoteca.redes_sociales) if discoteca.redes_sociales else {},
                'precio_entrada': float(discoteca.precio_entrada) if discoteca.precio_entrada else None,
                'latitud': float(discoteca.latitud) if discoteca.latitud else None,
                'longitud': float(discoteca.longitud) if discoteca.longitud else None,
                'servicios': discoteca.servicios,
                'estado_abierta': discoteca.estado_abierta,
                'promociones': discoteca.promociones
            })
        return JsonResponse({'discotecas': data})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def tasks_json(request):
    if request.method == 'GET':
        tasks = Project.objects.all()  # Obtiene todas las tareas del usuario autenticado
        data = []
        for task in tasks:
            data.append({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'fecha_creacion': task.created_at.strftime('%Y-%m-%d'),  # Formato de fecha
                'fecha_completado': task.datecompleted.strftime('%Y-%m-%d') if task.datecompleted else None,
                'username': task.user.username,
                'discoteca': task.discoteca.nombre,
            })
        return JsonResponse({'tasks': data})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def home(request):
    form = UserCreationForm()
    return render(request, 'home.html', {})

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
            else:
                print("Errores del formulario:", form.errors)
                return render(request, 'create_discoteca.html', {
                    'form': form,
                    'error': 'Por favor, provee datos válidos'
                })
        except ValueError as e:
            return render(request, 'create_discoteca.html', {
                'form': DiscotecaForm(),
                'error': f'Error al guardar la discoteca: {e}'
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


@login_required
def like_discoteca(request, discoteca_id):
    # Obtener la discoteca por su ID
    discoteca = get_object_or_404(Discoteca, pk=discoteca_id)

    # Si el usuario ya ha dado "like", lo quitamos (unlike)
    if request.user in discoteca.likes.all():
        discoteca.likes.remove(request.user)
    else:
        # Si el usuario no ha dado "like", lo agregamos
        discoteca.likes.add(request.user)

    # Redirigimos a la página de detalles de la discoteca
    return redirect('discoteca_detail', discoteca_id=discoteca.id)



