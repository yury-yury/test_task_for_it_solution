# Generated by Django 5.0 on 2023-12-07 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0002_alter_course_description_alter_student_courses"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="student",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]