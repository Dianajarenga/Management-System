# Generated by Django 3.2.5 on 2021-07-31 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='Lessons_per_month',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='Nationality',
            field=models.CharField(choices=[('R', 'Rwandese'), ('K', 'Kenyan'), ('Su', 'Sudanesse'), ('S', 'Somali'), ('SS', 'South Sudanese')], default=11, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='bank_account_no',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='company',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='contract',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='id_number',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='job_title',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='lessons_attendance',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='phone_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='profession',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='resume',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='syllabus',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
