from django.contrib import admin
from .forms import RegistradoForm
from .models import Registrado
# Register your models here.
class AdminRegistrado(admin.ModelAdmin):
	list_display = ["__str__","nombre","timestamp",]
	form = RegistradoForm
	# class Meta:
	# 	model = Registrado
admin.site.register(Registrado, AdminRegistrado)
			
