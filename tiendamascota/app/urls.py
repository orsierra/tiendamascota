from django.urls import path, include
from .views import agregar_mascota, home, producto, mascota,contacto, agregar_producto,\
    listar_productos, modificar_producto, eliminar_producto, registro, agregar_mascota,\
    listar_mascotas, modificar_mascota,eliminar_mascota, ProductoViewset,\
        mascota_collection, mascota_element      
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)


urlpatterns = [
    path('', home, name='home'),
    path('app/producto/', producto, name="producto"),
    path('mascota/', mascota, name="mascota"),
    path('contacto/', contacto, name="contacto"),
    
    ### Productos
    
    path('agregar-producto/', agregar_producto, name= "agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos" ),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    
    ## usuario  
    path('registro/', registro, name="registro"),
    ### Mascotas
    path('agregar-mascota/', agregar_mascota, name= "agregar_mascota"),
    path('listar-mascotas/', listar_mascotas, name="listar_mascotas" ),
    path('modificar-mascota/<id>/', modificar_mascota, name="modificar_mascota"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    
    ##rest_framework
    path('api/', include(router.urls)),     
        
    # api
    path('mascotas/',  mascota_collection , name='mascota_collection'),
    path('mascotas/<int:pk>/', mascota_element ,name='mascota_element'),

]