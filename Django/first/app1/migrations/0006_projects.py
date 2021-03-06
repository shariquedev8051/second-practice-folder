# Generated by Django 3.2.6 on 2021-08-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_task_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('projecet_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=15)),
                ('client', models.CharField(max_length=16)),
                ('employee', models.ManyToManyField(to='app1.Employee')),
            ],
            options={
                'db_table': 'emp_project',
            },
        ),
    ]
