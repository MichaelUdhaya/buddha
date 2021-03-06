# Generated by Django 3.0.3 on 2020-08-16 09:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_number', models.IntegerField()),
                ('exam_date', models.DateField(default=datetime.datetime.now)),
                ('syallbus', models.TextField(default='N/A')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('total_time', models.IntegerField(default=2, help_text='Duration for this question. Enter in Minutes')),
                ('mark_value', models.IntegerField(default=0, help_text='Enter mark value')),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.Course')),
            ],
        ),
    ]
