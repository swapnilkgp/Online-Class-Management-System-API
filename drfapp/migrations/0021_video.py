# Generated by Django 4.1.3 on 2023-03-31 04:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("drfapp", "0020_remove_message_id_message_msgid"),
    ]

    operations = [
        migrations.CreateModel(
            name="video",
            fields=[
                ("video", models.FileField(upload_to="")),
                ("caption", models.TextField()),
                ("senttime", models.DateTimeField()),
                (
                    "videoID",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="yourvideos",
                        to="drfapp.user",
                    ),
                ),
                (
                    "sendercourse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="videos",
                        to="drfapp.course",
                    ),
                ),
            ],
        ),
    ]