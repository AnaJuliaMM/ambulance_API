# Generated by Django 4.2.5 on 2023-09-16 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambulance', '0004_alter_ambulanceentity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulanceentity',
            name='chassi_code',
            field=models.CharField(max_length=17, unique=True),
        ),
        migrations.AlterField(
            model_name='ambulanceentity',
            name='license_plate',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]
