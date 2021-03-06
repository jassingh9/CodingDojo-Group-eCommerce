# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0017_auto_20170928_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ship_orders', to='ecommerce.Shipping'),
        ),
        migrations.AlterField(
            model_name='order',
            name='billing',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bill_orders', to='ecommerce.Billing'),
        ),
    ]
