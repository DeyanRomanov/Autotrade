# Generated by Django 3.2.12 on 2022-04-18 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220418_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='is_reviewed',
        ),
        migrations.RemoveField(
            model_name='motorcycle',
            name='is_reviewed',
        ),
        migrations.RemoveField(
            model_name='part',
            name='is_reviewed',
        ),
        migrations.RemoveField(
            model_name='truck',
            name='is_reviewed',
        ),
    ]
