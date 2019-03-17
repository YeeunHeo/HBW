# Generated by Django 2.1.5 on 2019-03-17 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20190316_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='now_time_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('start_time', models.PositiveSmallIntegerField(default=0)),
                ('is_manager', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='time_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('start_time', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='battery',
            name='borrowed_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ba', to='login.Student'),
        ),
        migrations.AlterField(
            model_name='cable',
            name='borrowed_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ca', to='login.Student'),
        ),
        migrations.AlterField(
            model_name='lan',
            name='borrowed_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='la', to='login.Student'),
        ),
        migrations.AlterField(
            model_name='studytable',
            name='lender',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='st', to='login.Student'),
        ),
    ]
