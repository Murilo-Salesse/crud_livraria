# Generated by Django 5.1.1 on 2024-10-05 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_livraria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
