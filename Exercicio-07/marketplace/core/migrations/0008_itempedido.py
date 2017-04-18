# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 06:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_itemvenda'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.IntegerField(default=0)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Produto')),
            ],
        ),
    ]
