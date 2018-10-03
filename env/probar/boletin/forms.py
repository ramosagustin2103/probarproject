from django import forms
from .models import Registrado

class RegistradoForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre", "email", "nombre", "email", "tipo_de_carga", "lugar_de_origen", "lugar_de_destino", "volumen_de_la_carga", "comentario"]

	nombre = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control ',
			'placeholder': 'Escribe un nombre de contacto...',
		}
	))
	email = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control ',
			'placeholder': 'Escribe un correo electronico para comunicarnos...',
		}
	))

	tipo_de_carga = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control ',
			'placeholder': 'Contanos que clase de carga debemos transportar...',
		}
	))
	lugar_de_origen = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control ',
			'placeholder': 'Contanos desde donde debe partir la carga...',
		}
	))
	lugar_de_destino = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control ',
			'placeholder': 'Contanos hasta donde debemos llevarla...',
		}
	))
	volumen_de_la_carga = forms.IntegerField(widget=forms.TextInput(
		attrs={
			'class': 'form-control ',
			'placeholder': 'Escribe el peso aproximado en kg y sin decimales...',			
		}
	))
	comentario = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Escribe alguna observacion o consulta si la tienes...',
		}
	))

	def __init__(self, *args, **kwargs):
		super(RegistradoForm, self).__init__(*args, **kwargs)

