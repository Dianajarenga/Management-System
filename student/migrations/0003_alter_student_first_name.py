# Generated by Django 3.2.4 on 2021-07-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210730_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='First_name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
