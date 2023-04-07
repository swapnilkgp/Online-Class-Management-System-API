# Generated by Django 4.1.3 on 2023-04-02 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drfapp", "0028_solution"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="TAs",
            field=models.ManyToManyField(
                related_name="courses_instructed", to="drfapp.user"
            ),
        ),
    ]
