# Generated by Django 3.2.6 on 2021-08-17 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
                ('adr', models.CharField(max_length=500)),
                ('company', models.CharField(default='infosys', max_length=100)),
            ],
            options={
                'db_table': 'emp',
            },
        ),
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('licence_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('expiry_data', models.DateField()),
                ('dl_type', models.CharField(max_length=10)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.employee')),
            ],
            options={
                'db_table': 'Licence',
            },
        ),
    ]
