# Generated by Django 2.2.6 on 2020-02-25 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0002_popmiss_popmister'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imeis',
            old_name='popu',
            new_name='popMiss',
        ),
        migrations.AddField(
            model_name='imeis',
            name='popMister',
            field=models.BooleanField(default=False),
        ),
    ]
