# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-25 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooggerapp', '0010_auto_20171025_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='telefon numarası,isteğe bağlı'),
        ),
    ]
