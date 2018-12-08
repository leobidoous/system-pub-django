from django.shortcuts import render
from core.forms import *
# Create your views here.
def mesa(request):
    data={'mesas': PedidoModel.objects.all(),
          'hidden': False}
    return render(request, 'mesa/mesa.html', data)

def nova_mesa(request):
    success = False
    form = CadastraPedidoForm(request.POST or None)
    if form.is_valid():
        form.novo_pedido()
        success = True
    data = {'form': form, 'success': success}
    return render(request, 'mesa/nova-mesa.html', data)

def detalhes_mesa(request, id):
    data = {'mesa': PedidoModel.objects.filter(id=id)}
    return render(request, 'mesa/detalhes-mesa.html', data)