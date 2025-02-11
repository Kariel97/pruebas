from django.contrib import admin
from .models import Clientes

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha_registro')

admin.site.register(Clientes, ClientesAdmin)
    
