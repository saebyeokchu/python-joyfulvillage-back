# Generated by Django 5.1 on 2025-03-12 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joyfulset', '0040_stay_layout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stay',
            name='layout',
        ),
    ]
