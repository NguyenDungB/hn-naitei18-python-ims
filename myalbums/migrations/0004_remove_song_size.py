# Generated by Django 3.1 on 2020-09-09 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myalbums', '0003_activity_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='size',
        ),
    ]
