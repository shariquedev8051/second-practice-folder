# Generated by Django 3.2.6 on 2021-08-22 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_projects_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='employee',
            field=models.ManyToManyField(db_column='emp_project', to='app1.Employee'),
        ),
    ]
