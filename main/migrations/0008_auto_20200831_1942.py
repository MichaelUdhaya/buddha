# Generated by Django 3.0.3 on 2020-08-31 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, default='Chennai', max_length=50),
        ),
    ]
