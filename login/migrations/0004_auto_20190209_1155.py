# Generated by Django 2.1.2 on 2019-02-09 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20190209_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studytable',
            name='eighth_time',
        ),
        migrations.AddField(
            model_name='studytable',
            name='eighth_time',
            field=models.ManyToManyField(blank=True, null=True, related_name='table_eighth_time', to='login.Student'),
        ),
        migrations.RemoveField(
            model_name='studytable',
            name='fifth_time',
        ),
        migrations.AddField(
            model_name='studytable',
            name='fifth_time',
            field=models.ManyToManyField(blank=True, null=True, related_name='table_fifth_time', to='login.Student'),
        ),
        migrations.RemoveField(
            model_name='studytable',
            name='first_time',
        ),
        migrations.AddField(
            model_name='studytable',
            name='first_time',
            field=models.ManyToManyField(blank=True, null=True, related_name='table_first_time', to='login.Student'),
        ),
        migrations.RemoveField(
            model_name='studytable',
            name='fourth_time',
        ),
        migrations.AddField(
            model_name='studytable',
            name='fourth_time',
            field=models.ManyToManyField(blank=True, null=True, related_name='table_fourth_time', to='login.Student'),
        ),
        migrations.RemoveField(
            model_name='studytable',
            name='second_time',
        ),
        migrations.AddField(
            model_name='studytable',
            name='second_time',
            field=models.ManyToManyField(blank=True, null=True, related_name='table_second_time', to='login.Student'),
        ),
        migrations.RemoveField(
            model_name='studytable',
            name='seventh_time',
        ),
        migrations.AddField(
            model_name='studytable',
            name='seventh_time',
            field=models.ManyToManyField(blank=True, null=True, related_name='table_seventh_time', to='login.Student'),
        ),
        migrations.RemoveField(
            model_name='studytable',
            name='sixth_time',
        ),
        migrations.AddField(
            model_name='studytable',
            name='sixth_time',
            field=models.ManyToManyField(blank=True, null=True, related_name='table_sixth_time', to='login.Student'),
        ),
        migrations.RemoveField(
            model_name='studytable',
            name='third_time',
        ),
        migrations.AddField(
            model_name='studytable',
            name='third_time',
            field=models.ManyToManyField(blank=True, null=True, related_name='table_third_time', to='login.Student'),
        ),
    ]