from django.urls import path
from .views import listar_clientes, agregar_cliente, crear_cliente, eliminar_cliente, actualizar_cliente, actualizar

urlpatterns = [
    path('listar_clientes/', listar_clientes, name="listar_clientes"),
    path('agregar_cliente/' , agregar_cliente, name="agregar_cliente"),
    path('crear_cliente/' , crear_cliente, name="crear_cliente"),
    path('actualizar_cliente/<int:id>' , actualizar_cliente, name="actualizar_cliente"),
    path('actualizar/<int:id>' , actualizar, name="actualizar"),
    path('eliminar_cliente/<int:id>' , eliminar_cliente, name="eliminar_cliente"),
]
