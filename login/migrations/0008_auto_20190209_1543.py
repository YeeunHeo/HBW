# Generated by Django 2.1.2 on 2019-02-09 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_battery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unbrella',
            name='borrowed_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Student'),
        ),
    ]
