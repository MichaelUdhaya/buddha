# Generated by Django 3.0.3 on 2020-08-06 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_profile_birthdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_number', models.IntegerField()),
                ('exam_date', models.DateField(default=datetime.datetime.now)),
                ('syallbus', models.TextField(default='N/A')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(default='1900-01-01'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='preparing_exam_from',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
