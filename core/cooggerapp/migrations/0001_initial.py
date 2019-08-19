# Generated by Django 2.0.12 on 2019-08-18 15:18

import django.db.models.deletion
import django_md_editor.models
from django.conf import settings
from django.db import migrations, models

import core.cooggerapp.models.common
import core.cooggerapp.models.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50)),
                (
                    "template",
                    django_md_editor.models.EditorMdField(blank=True, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Commit",
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
                (
                    "hash",
                    models.CharField(
                        default=core.cooggerapp.models.utils.get_new_hash,
                        max_length=256,
                        unique=True,
                    ),
                ),
                ("body", django_md_editor.models.EditorMdField()),
                ("msg", models.CharField(default="Initial commit", max_length=150)),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                ("reply_count", models.PositiveIntegerField(default=0)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("approved", "approved"),
                            ("rejected", "rejected"),
                            ("waiting", "waiting"),
                        ],
                        default="approved",
                        max_length=100,
                    ),
                ),
            ],
            options={"ordering": ["-created"]},
            bases=(core.cooggerapp.models.common.View, models.Model),
        ),
        migrations.CreateModel(
            name="Content",
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
                ("reply_count", models.PositiveIntegerField(default=0)),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "last_update",
                    models.DateTimeField(auto_now_add=True, verbose_name="Last update"),
                ),
                ("permlink", models.SlugField(max_length=200)),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="Be sure to choose the best title",
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "body",
                    django_md_editor.models.EditorMdField(
                        blank=True,
                        help_text="Your content | problem | question | or anything else",
                        null=True,
                        verbose_name="",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("arabic", "arabic"),
                            ("azerbaijani", "azerbaijani"),
                            ("chinese", "chinese"),
                            ("english", "english"),
                            ("french", "french"),
                            ("german", "german"),
                            ("indonesian", "indonesian"),
                            ("italian", "italian"),
                            ("japanese", "japanese"),
                            ("korean", "korean"),
                            ("polish", "polish"),
                            ("portuguese", "portuguese"),
                            ("romanian", "romanian"),
                            ("russian", "russian"),
                            ("spanish", "spanish"),
                            ("turkish", "turkish"),
                            ("vietnamese", "vietnamese"),
                        ],
                        help_text="The language of your content",
                        max_length=30,
                    ),
                ),
                (
                    "tags",
                    models.CharField(
                        help_text="Write your tags using spaces, max:5",
                        max_length=200,
                        verbose_name="Keywords",
                    ),
                ),
                ("image_address", models.URLField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("ready", "ready"), ("not-ready", "not ready")],
                        default="ready",
                        help_text="if your article isn't ready to publish yet, select 'not ready to publish'.",
                        max_length=30,
                        verbose_name="article's status",
                    ),
                ),
                (
                    "contributors_count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Total contributors count"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        help_text="select content category",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cooggerapp.Category",
                    ),
                ),
                (
                    "contributors",
                    models.ManyToManyField(
                        related_name="content_contributors", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-created"]},
            bases=(core.cooggerapp.models.common.View, models.Model),
        ),
        migrations.CreateModel(
            name="Issue",
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
                ("reply_count", models.PositiveIntegerField(default=0)),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "last_update",
                    models.DateTimeField(auto_now_add=True, verbose_name="Last update"),
                ),
                ("issue_id", models.PositiveIntegerField(default=0)),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="Be sure to choose the best title",
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "body",
                    django_md_editor.models.EditorMdField(
                        blank=True,
                        help_text="Your problem | question | or anything else",
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[("open", "open"), ("closed", "closed")],
                        default="open",
                        help_text="Status",
                        max_length=55,
                        null=True,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-created"]},
            bases=(core.cooggerapp.models.common.View, models.Model),
        ),
        migrations.CreateModel(
            name="OtherAddressesOfUsers",
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
                (
                    "choices",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("facebook", "facebook"),
                            ("github", "github"),
                            ("instagram", "instagram"),
                            ("linkedin", "linkedin"),
                            ("twitter", "twitter"),
                            ("web-site", "web site"),
                            ("youtube", "youtube"),
                        ],
                        max_length=15,
                        null=True,
                        verbose_name="website",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="write address / username",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReportModel",
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
                (
                    "complaints",
                    models.CharField(
                        choices=[
                            ("fraud-or-plagiarism", "fraud or plagiarism"),
                            (
                                "hate-speech-or-internet-trolling",
                                "hate speech or internet trolling",
                            ),
                            (
                                "intentional-miss-categorized-content-or-spam",
                                "intentional miss-categorized content or spam",
                            ),
                            (
                                "i-think-this-content-should-not-be-at-coogger",
                                "i think this content should not be at coogger",
                            ),
                            (
                                "this-content-is-not-tutorial-content",
                                "this content is not tutorial content",
                            ),
                            ("wrong-list-name", "wrong list name"),
                        ],
                        max_length=40,
                        verbose_name="type of report",
                    ),
                ),
                (
                    "add",
                    models.CharField(
                        blank=True,
                        max_length=600,
                        null=True,
                        verbose_name="Can you give more information ?",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "content",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cooggerapp.Content",
                        verbose_name="reported person",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="reporter",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SearchedWords",
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
                ("word", models.CharField(max_length=100, unique=True)),
                ("hmany", models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name="Topic",
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
                (
                    "name",
                    models.CharField(
                        help_text="Please, write topic name.",
                        max_length=50,
                        verbose_name="Name",
                    ),
                ),
                ("permlink", models.SlugField(max_length=200)),
                (
                    "image_address",
                    models.URLField(
                        blank=True,
                        help_text="Add an Image Address",
                        max_length=400,
                        null=True,
                    ),
                ),
                (
                    "definition",
                    models.CharField(
                        blank=True,
                        help_text="Definition of topic",
                        max_length=600,
                        null=True,
                    ),
                ),
                (
                    "tags",
                    models.CharField(
                        blank=True,
                        help_text="Write your tags using spaces",
                        max_length=200,
                        null=True,
                        verbose_name="Keyword",
                    ),
                ),
                (
                    "address",
                    models.URLField(
                        blank=True,
                        help_text="Add an address if it have",
                        max_length=150,
                        null=True,
                    ),
                ),
                (
                    "how_many",
                    models.PositiveIntegerField(
                        default=0, verbose_name="How many content in"
                    ),
                ),
                (
                    "editable",
                    models.BooleanField(
                        default=True, verbose_name="Is it editable? | Yes/No"
                    ),
                ),
            ],
            options={"verbose_name_plural": "Global Topic", "ordering": ["-how_many"]},
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "about",
                    django_md_editor.models.EditorMdField(
                        blank=True,
                        help_text="Write a long article about yourself, see; /u/@your_username/about/",
                        null=True,
                        verbose_name="About Yourself",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="Write something short about yourself, this will appear in your profile.",
                        max_length=260,
                        null=True,
                    ),
                ),
                (
                    "email_permission",
                    models.BooleanField(
                        default=True, help_text="Allow email notifications."
                    ),
                ),
                (
                    "address",
                    models.ManyToManyField(
                        blank=True, to="cooggerapp.OtherAddressesOfUsers"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UTopic",
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
                (
                    "name",
                    models.CharField(
                        help_text="Please, write topic name.",
                        max_length=50,
                        verbose_name="Name",
                    ),
                ),
                ("permlink", models.SlugField(max_length=200)),
                (
                    "image_address",
                    models.URLField(
                        blank=True,
                        help_text="Add an Image Address",
                        max_length=400,
                        null=True,
                    ),
                ),
                (
                    "definition",
                    models.CharField(
                        blank=True,
                        help_text="Definition of topic",
                        max_length=600,
                        null=True,
                    ),
                ),
                (
                    "tags",
                    models.CharField(
                        blank=True,
                        help_text="Write your tags using spaces",
                        max_length=200,
                        null=True,
                        verbose_name="Keyword",
                    ),
                ),
                (
                    "address",
                    models.URLField(
                        blank=True,
                        help_text="Add an address if it have",
                        max_length=150,
                        null=True,
                    ),
                ),
                (
                    "how_many",
                    models.PositiveIntegerField(
                        default=0, verbose_name="How many content in"
                    ),
                ),
                (
                    "total_dor",
                    models.FloatField(
                        default=0, verbose_name="Total duration all contents"
                    ),
                ),
                (
                    "total_view",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Total views all contents"
                    ),
                ),
                (
                    "open_issue",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Total count open issue"
                    ),
                ),
                (
                    "closed_issue",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Total count closed issue"
                    ),
                ),
                (
                    "open_contribution",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Total count open contributions"
                    ),
                ),
                (
                    "closed_contribution",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Total count closed contributions"
                    ),
                ),
                (
                    "contributors_count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Total contributors count"
                    ),
                ),
                (
                    "commit_count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Total commit count"
                    ),
                ),
                (
                    "contributors",
                    models.ManyToManyField(
                        related_name="utopic_contributors", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name_plural": "User Topic", "ordering": ["-how_many"]},
        ),
        migrations.AlterUniqueTogether(name="topic", unique_together={("permlink",)}),
        migrations.AddField(
            model_name="issue",
            name="utopic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cooggerapp.UTopic"
            ),
        ),
        migrations.AddField(
            model_name="content",
            name="utopic",
            field=models.ForeignKey(
                help_text="Please, write your topic about your contents.",
                on_delete=django.db.models.deletion.CASCADE,
                to="cooggerapp.UTopic",
                verbose_name="Your topic",
            ),
        ),
        migrations.AddField(
            model_name="commit",
            name="content",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cooggerapp.Content"
            ),
        ),
        migrations.AddField(
            model_name="commit",
            name="previous_commit",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="cooggerapp.Commit",
            ),
        ),
        migrations.AddField(
            model_name="commit",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="commit",
            name="utopic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cooggerapp.UTopic"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="utopic", unique_together={("user", "permlink")}
        ),
        migrations.AlterUniqueTogether(
            name="issue", unique_together={("user", "issue_id", "utopic")}
        ),
        migrations.AlterUniqueTogether(
            name="content", unique_together={("user", "permlink")}
        ),
    ]
