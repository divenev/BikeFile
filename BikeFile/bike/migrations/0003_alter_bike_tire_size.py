# Generated by Django 4.2.3 on 2024-05-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0002_rename_owner_id_bike_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='tire_size',
            field=models.FloatField(verbose_name='tire size'),
        ),
    ]
