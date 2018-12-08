from django.shortcuts import render
from django.views import generic
from core.forms import *

# Create your views here.
class FuncionarioListView(generic.ListView):
    pass
def funcionario(request):
    data = {}
    data['funcionarios'] = FuncionarioModel.objects.all()
    return render(request, 'funcionario/funcionario.html', data)

def cadastrar_funcionario(request):
    success = False
    form = CadastraFuncionarioForm(request.POST or None)
    if form.is_valid():
        form.novo_funcionario()
        success = True
    data = {'form': form, 'success': success}
    return render(request, 'funcionario/cadastrar-funcionario.html', data)
