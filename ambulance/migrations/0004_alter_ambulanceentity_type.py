# Generated by Django 4.2.5 on 2023-09-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambulance', '0003_alter_ambulanceentity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulanceentity',
            name='type',
            field=models.CharField(choices=[('a', 'Basic Life Support Ambulance'), ('b', 'Intermediate Life Support Ambulance'), ('c', 'Advanced Life Support Ambulance')], max_length=100),
        ),
    ]