# Generated by Django 2.1.3 on 2018-12-07 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesa', '0002_auto_20181207_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidomodel',
            name='Produto_Hokaah',
            field=models.ManyToManyField(null=True, to='hookah.ProdutoHookahModel'),
        ),
        migrations.AlterField(
            model_name='pedidomodel',
            name='Produto_Pub',
            field=models.ManyToManyField(null=True, to='pub.ProdutoPubModel'),
        ),
    ]
