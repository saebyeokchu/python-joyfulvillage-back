# Generated by Django 5.1 on 2025-01-16 23:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='program',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('subName', models.TextField()),
                ('content', models.TextField()),
                ('lastModifiedAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
