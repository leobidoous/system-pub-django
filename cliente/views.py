from django.shortcuts import render
from core.forms import *
from cliente.models import *

# Create your views here.
def cliente(request):
    data = {}
    data['clientes'] = ClienteModel.objects.all()
    return render(request, 'cliente/cliente.html', data)

def cadastrar_cliente(request):
    success = False
    form = CadastraClienteForm(request.POST or None)
    if form.is_valid():
        form.novo_cliente()
        form.clean()
        success = True
    data = {'form': form, 'success': success}
    return render(request, 'cliente/cadastrar-cliente.html', data)