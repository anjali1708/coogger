# Generated by Django 3.0 on 2019-12-16 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("ip", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DjangoViews",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.PositiveIntegerField()),
                ("views_count", models.IntegerField(default=0)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                    ),
                ),
                ("ips", models.ManyToManyField(to="ip.IpModel")),
            ],
        )
    ]
