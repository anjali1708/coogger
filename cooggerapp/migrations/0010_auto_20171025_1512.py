# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-25 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooggerapp', '0009_auto_20171023_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='telefon numarası'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content_list',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Liste ismi'),
        ),
        migrations.AlterField(
            model_name='userfollow',
            name='user',
            field=models.CharField(choices=[('coogger', 'coogger'), ('hakancelik', 'hakancelik'), ('ibrahimsmngl', 'ibrahimsmngl'), ('ufukozer', 'ufukozer'), ('baristutakli', 'baristutakli'), ('imerafera', 'imerafera'), ('fadimekaplan', 'fadimekaplan'), ('vayra53', 'vayra53'), ('teibe', 'teibe'), ('ooznur', 'ooznur'), ('arslan', 'arslan'), ('saiddemir', 'saiddemir'), ('dersim67', 'dersim67'), ('volkan_dere', 'volkan_dere'), ('murecoder', 'murecoder')], max_length=37),
        ),
    ]
