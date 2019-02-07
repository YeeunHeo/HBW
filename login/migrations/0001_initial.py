# Generated by Django 2.1.2 on 2019-02-07 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('is_borrowed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Lan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('is_borrowed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_year', models.CharField(max_length=8)),
                ('is_paid', models.BooleanField(default=False)),
                ('today_A4', models.PositiveIntegerField(default=0)),
                ('month_A4', models.PositiveIntegerField(default=0)),
                ('battery', models.BooleanField(default=False)),
                ('lan', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_data', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudyTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('is_borrowed', models.BooleanField(default=False)),
                ('eighth_time', models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='table_eighth_time', to='login.Student')),
                ('fifth_time', models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='table_fifth_time', to='login.Student')),
                ('first_time', models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='table_first_time', to='login.Student')),
                ('fourth_time', models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='table_fourth_time', to='login.Student')),
                ('second_time', models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='table_second_time', to='login.Student')),
                ('seventh_time', models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='table_seventh_time', to='login.Student')),
                ('sixth_time', models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='table_sixth_time', to='login.Student')),
                ('third_time', models.OneToOneField(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='table_third_time', to='login.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Unbrella',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('is_borrowed', models.BooleanField(default=False)),
                ('borrowed_by', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unbrella_borrwed_by', to='login.Student')),
            ],
        ),
        migrations.AddField(
            model_name='lan',
            name='borrowed_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lan_borrowed_by', to='login.Student'),
        ),
        migrations.AddField(
            model_name='battery',
            name='borrowed_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='battery_borrowed_by', to='login.Student'),
        ),
    ]
