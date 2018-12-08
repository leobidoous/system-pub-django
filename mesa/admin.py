from django.contrib import admin
from mesa.models import *
# Register your models here.
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','create_at', 'update_at']
    search_fields = ['id', 'create_at', 'update_at']

admin.site.register(PedidoModel, PedidoAdmin)
