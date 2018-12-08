# Generated by Django 2.1.2 on 2018-12-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pessoamodel',
            options={'ordering': ['nome'], 'verbose_name': 'Pessoa', 'verbose_name_plural': 'Pessoas'},
        ),
        migrations.RemoveField(
            model_name='pessoamodel',
            name='funcao',
        ),
        migrations.AlterField(
            model_name='pessoamodel',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='pessoamodel',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
    ]