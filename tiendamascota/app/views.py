from dataclasses import dataclass
from urllib.request import Request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, Producto
from .forms import ContactoForm, ProductoForm, MascotaForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework  import viewsets
from .serializers import ProductoSerializer, MascotaSerializer


from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 



#### Seriliazer Producto
class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

### Pagina
def home(request):
    return render(request, 'app/home.html')

def producto(request):
    productos =  Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/producto.html',data)

def mascota(request):
    mascotas =  Mascota.objects.all()
    data = {
        'mascotas': mascotas
    }
    return render(request, 'app/mascota.html',data)
### COntacto formulario
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    return  render(request, 'app/contacto.html', data)

#####   AGREGAR PRODUCTO   #########

@login_required
def agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/listar-productos")
    else:
        form = ProductoForm()
        return render(request, "app/producto/agregar.html", {'form': form})


#####   Listar PRODUCTOS   #########
def listar_productos(request):
    productos = Producto.objects.all()
    
    data = {
        'productos' : productos
    }
    return render(request, 'app/producto/listar.html', data)


####  Modificar Producto
@login_required   
def modificar_producto(request, id):
    instancia = Producto.objects.get(id=id)

    form = ProductoForm(instance=instancia)

    if request.method == "POST":
        form = ProductoForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()

    return render(request, "app/producto/modificar.html", {'form': form})


###### Eliminar producto####
@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_productos")

#### Mascotas##

#####   AGREGAR Mascota   #########

@login_required
def agregar_mascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/listar-mascotas")
    else:
        form = MascotaForm()
        return render(request, "app/mascota/agregar.html", {'form': form})


#####   Listar Mascota   #########
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    
    data = {
        'mascotas' : mascotas
    }
    return render(request, 'app/mascota/listar.html', data)


####  Modificar mascota
@login_required   
def modificar_mascota(request, id):
    instancia = Mascota.objects.get(id=id)

    form = MascotaForm(instance=instancia)

    if request.method == "POST":
        form = MascotaForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()

    return render(request, "app/mascota/modificar.html", {'form': form})


###### Eliminar mascota####
@login_required
def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    mascota.delete()
    return redirect(to="listar_mascotas")



### Registro de usuario
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data['form']  = formulario  
            
    return render(request, 'Registration/registro.html', data)


###Serializer Mascota

# se pase a la función de vista. En este momento, solo admitimos solicitudes GET
@api_view(['GET'])
def mascota_collection(request):
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)


    
@api_view(['GET', 'PUT', 'DELETE'])
def mascota_element(request, pk):
    mascota = get_object_or_404(Mascota, id=pk)

    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        mascota_new = JSONParser().parse(request) 
        serializer = MascotaSerializer(mascota, data=mascota_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

