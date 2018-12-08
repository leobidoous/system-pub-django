from django.contrib import admin
from cliente.models import *

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'create_at', 'update_at']
    search_fields = ['nome']

admin.site.register(ClienteModel, ClienteAdmin)
