from django import forms
from mesa.models import PedidoModel
from cliente.models import ClienteModel
from funcionario.models import FuncionarioModel
from pub.models import ProdutoPubModel
from hookah.models import ProdutoHookahModel
from mesa.models import PedidoModel

class NovaMesa(forms.Form):
    pass

class CadastraProdutoHookaForm(forms.ModelForm):
    class Meta:
        model = ProdutoHookahModel
        fields = ('nome', 'preco', 'produto')

    def novo_produto_hookah(self):
        nome = self.cleaned_data['nome']
        preco = self.cleaned_data['preco']
        produto = self.cleaned_data['produto']
        self.save()

class CadastraProdutoPubForm(forms.ModelForm):
    class Meta:
        model = ProdutoPubModel
        fields = ('nome', 'preco', 'produto')

    def novo_produto_pub(self):
        nome = self.cleaned_data['nome']
        preco = self.cleaned_data['preco']
        produto = self.cleaned_data['produto']
        self.save()

class CadastraFuncionarioForm(forms.ModelForm):
    class Meta:
        model = FuncionarioModel
        fields = ('nome', 'cpf', 'funcao')

    def novo_funcionario(self):
        nome = self.cleaned_data['nome']
        cpf = self.cleaned_data['cpf']
        funcao = self.cleaned_data['funcao']
        self.save()

class CadastraClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteModel
        fields = ('nome', 'cpf')

    def novo_cliente(self):
        nome = self.cleaned_data['nome']
        cpf = self.cleaned_data['cpf']
        self.save()
        self.clean()

class CadastraPedidoForm(forms.ModelForm):
    class Meta:
        model = PedidoModel
        fields = ('Funcionario', 'Cliente', 'Produto_Hookah', 'Produto_Pub')

    def novo_pedido(self):
        self.save()
