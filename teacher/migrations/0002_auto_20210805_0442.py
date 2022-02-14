# Generated by Django 3.2.5 on 2021-08-05 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='fac_resume',
            new_name='certificate',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='certification',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='id_proof_image',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='qualification',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='total_experience',
        ),
        migrations.AddField(
            model_name='teacher',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='edu_qualification',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='id_proof',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_adharcard',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_pancard',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_passport',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='tch_information',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='tch_resume',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='competency_area',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
