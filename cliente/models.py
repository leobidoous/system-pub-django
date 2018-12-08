from django.db import models
from django.urls import reverse

# Create your models here.
class ClienteModel(models.Model):
    nome = models.CharField('Nome Cliente', max_length=100)
    cpf = models.CharField('CPF Cliente', max_length=14, unique=True)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return self.nome

    def get_absolut_url(self):
        return reverse('list_view', kwargs={'cliente':self.nome})
