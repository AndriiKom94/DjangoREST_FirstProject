# Generated by Django 3.1.6 on 2021-02-10 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Vin'),
        ),
    ]
