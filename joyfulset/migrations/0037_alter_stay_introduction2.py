# Generated by Django 5.1 on 2025-03-05 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joyfulset', '0036_rename_introduction_stay_introduction1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stay',
            name='introduction2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
