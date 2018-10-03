from django.db import models
# Create your models here.


class Registrado(models.Model):
	nombre = models.CharField(max_length=120, blank=True ,null=True)
	email = models.EmailField()
	codigo_postal = models.IntegerField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)
	media = models.FileField(upload_to = 'myfolder/', blank=True, null=True) 
	tipo_de_carga = models.CharField(max_length=120, blank=True ,null=True)
	lugar_de_origen = models.CharField(max_length=120, blank=True ,null=True)
	lugar_de_destino = models.CharField(max_length=120, blank=True ,null=True)
	volumen_de_la_carga = models.IntegerField(blank=True, null=True)
	comentario = models.TextField(max_length=400, blank=True ,null=True)

	"""docstring for registrado"""
	def __str__(self):
		return self.email
		


		