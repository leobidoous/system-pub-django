from django.db import models
from django.urls import reverse

# Create your models here.
class ProdutoPubModel(models.Model):
    nome = models.CharField('Nome Produto', max_length=100, unique=True)
    preco = models.FloatField('Preço Produto')
    produto = models.SlugField('Slug Produto', max_length=100)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolut_url(self):
        return reverse('list_view', kwargs={'produto':self.nome})
