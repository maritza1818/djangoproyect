from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
def home(request):
    form = UserCreationForm()
    return render(request, 'home.html', {
    })
def signup(request):
    if( request.method == 'GET'):
        print('enviando formulario')
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrando usuaeuo+
            try:
                user = User.objects.create_user(username=request.POST['username'],password = request.POST['password1'])
                user.save()
                return HttpResponse('User created sucessfully')
            except:
                return HttpResponse('Username already exists')
        return HttpResponse('Password do not match')
        print(request.POST)
        print('obteniendo resultados')
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })