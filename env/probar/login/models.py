from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='myfolder/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username




class Registro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    valor = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    peso = models.CharField(max_length=20, blank=True)
    distancia = models.CharField(max_length=20, blank=True)

    
    def __str__(self):
        return self.user.valor


class Precios(models.Model):
    precio_x_km_1 = models.CharField(max_length=20, blank=True)
    precio_x_km_2 = models.CharField(max_length=20, blank=True)
    precio_x_km_3 = models.CharField(max_length=20, blank=True)
    limite_1 = models.CharField(max_length=20, blank=True)
    limite_2 = models.CharField(max_length=20, blank=True)
    limite_3 = models.CharField(max_length=20, blank=True)
 
   
