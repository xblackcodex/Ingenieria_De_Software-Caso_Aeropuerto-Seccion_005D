from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria
from .models import Vehiculo


class VehiculoForm(forms.ModelForm):

    class Meta: 
        model = Vehiculo
        fields = ['patente', 'chofer', 'modelo', 'ubicacionsal', 'cantdisponible']
        labels ={
            'patente': 'Patente', 
            'chofer': 'Chofer', 
            'modelo': 'Modelo', 
            'ubicacionsal': 'Ubicacionsal',
            'cantdisponible' : 'Cantdisponible',
        }
        widgets={
            'patente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la patente', 
                    'id': 'patente'
                }
            ), 
            'chofer': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el chofer', 
                    'id': 'chofer'
                }
            ), 
            'modelo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese modelo del vehiculo', 
                    'id': 'modelo'
                }
            ), 
            'ubicacionsal': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la ubicacion de salida', 
                    'id': 'ubicacionsal'
                }
            ), 
            'cantdisponible': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'cantdisponible',
                }
            )

        }
