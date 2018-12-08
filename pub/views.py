from django.shortcuts import render
from core.forms import *

# Create your views here.
def pub(request):
    data = {}
    data['produtos'] = ProdutoPubModel.objects.all()
    return render(request, 'pub/pub.html', data)

def cadastrar_produto_pub(request):
    success = False
    form = CadastraProdutoPubForm(request.POST or None)
    if form.is_valid():
        form.novo_produto_pub()
        success = True
    data = {'form': form, 'success': success}
    return  render(request, 'pub/cadastrar-produto-pub.html', data)