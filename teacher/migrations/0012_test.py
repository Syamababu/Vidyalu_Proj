# Generated by Django 3.2.5 on 2021-11-02 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0011_course_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='test subject', max_length=500)),
                ('no_of_question', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
            options={
                'db_table': 'teacher_tests',
            },
        ),
    ]
