from dataclasses import fields
from django import forms
from.models import Mascota, Contacto, Producto
from django.contrib.auth.forms import UserCreationForm   
from django.contrib.auth.models import User

class MascotaForm(forms.ModelForm):
    class Meta:
        model=Mascota
        fields = '__all__' 

        
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__' 

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields= '__all__' 

class CustomUserCreationForm(UserCreationForm):
        
        class Meta:
            model = User
            fields = ['username', "first_name", "last_name", "email", "password1", "password2"]