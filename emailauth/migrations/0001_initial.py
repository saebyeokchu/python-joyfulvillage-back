# Generated by Django 5.1 on 2025-01-05 05:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eamilAddress', models.CharField(max_length=50)),
                ('authCode', models.CharField(max_length=6)),
                ('verified', models.BooleanField(default=False)),
                ('lastModifiedAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
