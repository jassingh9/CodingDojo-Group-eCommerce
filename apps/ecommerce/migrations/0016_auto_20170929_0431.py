# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_merge_20170929_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity_purchased',
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(related_name='item', to='ecommerce.Item'),
        ),
    ]
