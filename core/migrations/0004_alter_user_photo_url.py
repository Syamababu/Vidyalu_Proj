# Generated by Django 3.2.5 on 2021-08-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo_url',
            field=models.CharField(default='', max_length=199),
        ),
    ]