# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_auto_20170928_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_in_cart', to='ecommerce.Item'),
        ),
    ]
