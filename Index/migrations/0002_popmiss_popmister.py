# Generated by Django 2.2.6 on 2020-02-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopMiss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmiss', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PopMister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmis', models.IntegerField()),
            ],
        ),
    ]
