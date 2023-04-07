# Generated by Django 4.1.3 on 2023-03-29 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drfapp", "0015_alter_course_coursecode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="students",
            field=models.ManyToManyField(
                related_name="courses_learnt", to="drfapp.user"
            ),
        ),
    ]