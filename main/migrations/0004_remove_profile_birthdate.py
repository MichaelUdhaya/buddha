# Generated by Django 3.0.3 on 2020-08-03 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
    ]
