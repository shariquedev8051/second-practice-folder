# Generated by Django 3.2.6 on 2021-08-22 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('price', models.IntegerField()),
                ('is_published', models.BooleanField(default=False)),
                ('published_date', models.DateField(null=True)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
