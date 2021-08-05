# Generated by Django 3.2.5 on 2021-08-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_material',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='course_syllabus',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='trainers_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
