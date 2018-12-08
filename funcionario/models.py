from django.db import models
from django.urls import reverse

# Create your models here.
class FuncionarioModel(models.Model):
    nome = models.CharField('Nome Funcionário', max_length=100)
    cpf = models.CharField('CPF Funcionário', max_length=14, unique=True)
    funcao = models.SlugField('Função', max_length=100)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolut_url(self):
        return reverse('list_view', kwargs={'funcionario':self.nome})