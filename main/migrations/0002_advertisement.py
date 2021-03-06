# Generated by Django 3.0.3 on 2020-08-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_name', models.CharField(max_length=150)),
                ('ad_photo', models.ImageField(upload_to='ads/%Y/%m/%d/')),
                ('ad_updated_date', models.DateField(auto_now_add=True)),
                ('ad_expire_date', models.DateField()),
            ],
        ),
    ]
