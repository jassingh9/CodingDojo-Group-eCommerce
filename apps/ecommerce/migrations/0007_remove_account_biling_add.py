# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_remove_account_shipping_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='biling_add',
        ),
    ]
