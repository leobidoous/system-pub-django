from django.db import models
from django.urls import reverse
from hookah.models import ProdutoHookahModel
from pub.models import ProdutoPubModel
from funcionario.models import FuncionarioModel
from cliente.models import ClienteModel

# Create your models here.
class PedidoModel(models.Model):
    Funcionario = models.ForeignKey(FuncionarioModel, on_delete=models.CASCADE)
    Cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE)
    Produto_Hookah = models.ManyToManyField(ProdutoHookahModel, blank=True)
    Produto_Pub = models.ManyToManyField(ProdutoPubModel, blank=True)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

    def __str__(self):
        return 'PedidoHookahModel'

    def get_absolut_url(self):
        return reverse('list_view', kwargs={'pedido': self.Funcionario})