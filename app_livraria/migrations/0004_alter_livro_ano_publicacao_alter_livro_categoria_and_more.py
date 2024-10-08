# Generated by Django 5.1.1 on 2024-10-05 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_livraria', '0003_autor_categoria_livro_autor_livro_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='ano_publicacao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_livraria.categoria'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
