# Generated by Django 4.2.5 on 2023-09-21 01:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_reservas_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 9, 21, 1, 24, 19, 846633, tzinfo=datetime.timezone.utc)),
        ),
    ]
