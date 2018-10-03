from django.conf import settings 
from django.shortcuts import render

from .models import Registrado
from .forms import RegistradoForm
from django.core.mail import send_mail


def contacto(request):
	titulo = 'contacto'
	formulario = RegistradoForm(request.POST or None, request.FILES or None)
	context = {
		"titulo": titulo,
		"formulario" : formulario	
	}

	if formulario.is_valid():	
		nombre = formulario.cleaned_data.get("nombre")
		email = formulario.cleaned_data.get("email")
		volumen_de_la_carga = formulario.cleaned_data.get("volumen_de_la_carga")
		lugar_de_origen = formulario.cleaned_data.get("lugar_de_origen")
		lugar_de_destino = formulario.cleaned_data.get("lugar_de_destino")
		comentario = formulario.cleaned_data.get("comentario")

		asunto = 'un asunto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from]
		email_mensaje = "nombre: %s,  email: %s,  lugar de origen: %s,  lugar de destino: %s,  volumen de la carga: %skg,  comentario: %s" %(nombre, email, lugar_de_origen, lugar_de_destino, volumen_de_la_carga, comentario)
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently=True
			)
		formulario.save()
		return render(request, "contacto_realizado.html", context)

	return render(request, "contacto.html", context)


