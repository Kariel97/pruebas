from django.contrib import admin
from .models import Clientes

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')

admin.site.register(Clientes, ClientesAdmin)
    
