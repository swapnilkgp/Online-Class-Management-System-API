# Generated by Django 4.1.3 on 2023-03-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drfapp", "0004_delete_userlogin_rename_id_user_userid"),
    ]

    operations = [
        migrations.CreateModel(
            name="course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("courseno", models.CharField(max_length=100)),
                ("coursename", models.TextField()),
                ("coursecode", models.CharField(max_length=9, unique=True)),
            ],
        ),
    ]
