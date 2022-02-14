# Generated by Django 3.2.5 on 2021-12-06 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0002_auto_20211206_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemNotification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('notification', models.TextField(default='System Notification Creation failed')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'system_notification',
            },
        ),
    ]
