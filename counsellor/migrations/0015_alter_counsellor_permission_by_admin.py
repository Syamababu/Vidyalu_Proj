# Generated by Django 3.2.5 on 2022-01-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellor', '0014_auto_20211228_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counsellor',
            name='permission_by_admin',
            field=models.BooleanField(default=False),
        ),
    ]
