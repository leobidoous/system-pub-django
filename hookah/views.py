from django.shortcuts import render
from core.forms import *

# Create your views here.
def hookah(request):
    data = {}
    data['produtos'] = ProdutoHookahModel.objects.all()
    return render(request, 'hookah/hookah.html', data)

def cadastrar_produto_hookah(request):
    success = False
    form = CadastraProdutoHookaForm(request.POST or None)
    if form.is_valid():
        form.novo_produto_hookah()
        success = True
    data = {'form': form, 'success': success}
    return render(request, 'hookah/cadastrar-produto-hookah.html', data)