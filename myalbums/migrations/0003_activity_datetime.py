# Generated by Django 3.1 on 2020-09-06 03:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myalbums', '0002_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
