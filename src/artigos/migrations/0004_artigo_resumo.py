# Generated by Django 5.2.1 on 2025-05-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0003_pedidocolaboracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='resumo',
            field=models.TextField(blank=True, verbose_name='Resumo do artigo'),
        ),
    ]
