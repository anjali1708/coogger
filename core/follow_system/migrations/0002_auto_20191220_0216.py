# Generated by Django 2.2.8 on 2019-12-19 23:16

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("follow_system", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="follow",
            name="created",
            field=models.DateTimeField(default=datetime.datetime.now),
        )
    ]
