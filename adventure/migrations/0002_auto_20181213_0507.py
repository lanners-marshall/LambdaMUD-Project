# Generated by Django 2.1.4 on 2018-12-13 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='items',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='room',
            name='items',
            field=models.CharField(default='', max_length=500),
        ),
    ]
