from django.contrib import admin
from funcionario.models import *

# Register your models here.
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'funcao', 'create_at', 'update_at']
    search_fields = ['nome', 'funcao']
    list_filter = ['funcao', 'create_at', 'update_at']

admin.site.register(FuncionarioModel, FuncionarioAdmin)
