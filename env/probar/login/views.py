from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Exception
from django.db.utils import IntegrityError

from django.contrib.auth.models import User
from .models import Profile, Registro, Precios
from boletin.models import Registrado








def login_views(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            profile = request.user.profile
            if profile.is_admin == True:
                return redirect('administracion')
            else:
                login(request, user)
                return redirect('calcular_costos')

        else:
            return render(request, 'login.html', {'error': 'USUARIO O CONTRASEÑA INVALIDOS'})

    return render(request, 'login.html')




@login_required
def calcular_costos(request):
    titulo = 'calcular_costos'
    profile = request.user.profile
    registro = Registro.objects.filter(profile = profile)
    precio = Precios.objects.all()
    context={
    "titulo": titulo,
    'registros' : registro,
    'precios' : precio 
    }
    return render(request, "calcular_costos.html", context)







def logout_views(request):
    """Logout a user."""
    logout(request)
    return redirect('login_views')



def signup_views(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        picture = request.FILES['picture']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'signup.html', {'error': 'Contraseña incorrecta'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'El usuario ya existe'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user, phone_number=phone_number, picture=picture)
        profile.save()

        return redirect('login_views')

    return render(request, 'signup.html')






def guardar(request):
    if request.method == 'POST':
        valor = request.POST['valor']
        peso = request.POST['peso']
        distancia = request.POST['distancia']
        user = request.user
        profile = request.user.profile
        registro = Registro.objects.create(valor=valor, profile=profile, user=user, peso=peso, distancia=distancia)
        return redirect('calcular_costos')





@login_required
def administracion(request):
    titulo = 'administracion'
    perfil = Profile.objects.all()
    contacto = Registrado.objects.all()
    precio = Precios.objects.all()
    context={
    "titulo": titulo,
    'perfiles' : perfil,
    "contactos" : contacto,
    'precios' : precio 
    }
    return render(request, "administracion.html", context)




def precios(request):
    if request.method == 'POST':
        precio_x_km_1 = request.POST['precio_x_km_1']
        precio_x_km_2 = request.POST['precio_x_km_2']
        precio_x_km_3 = request.POST['precio_x_km_3']
        limite_1 = request.POST['limite_1']
        limite_2 = request.POST['limite_2']
        limite_3 = request.POST['limite_3']
        precios = Precios.objects.update(precio_x_km_1=precio_x_km_1, precio_x_km_2=precio_x_km_2, precio_x_km_3=precio_x_km_3, limite_1=limite_1, limite_2=limite_2, limite_3=limite_3)
        return redirect('administracion')

