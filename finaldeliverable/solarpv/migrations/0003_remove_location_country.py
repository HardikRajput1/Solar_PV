# Generated by Django 3.2.5 on 2021-11-28 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solarpv', '0002_auto_20211128_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='country',
        ),
    ]
