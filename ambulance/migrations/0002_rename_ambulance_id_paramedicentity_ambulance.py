# Generated by Django 4.2.4 on 2023-08-29 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ambulance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paramedicentity',
            old_name='ambulance_id',
            new_name='ambulance',
        ),
    ]