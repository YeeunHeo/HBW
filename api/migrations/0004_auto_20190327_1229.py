# Generated by Django 2.1.2 on 2019-03-27 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_logging_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logging',
            name='date',
        ),
        migrations.RemoveField(
            model_name='logging',
            name='manager',
        ),
    ]
