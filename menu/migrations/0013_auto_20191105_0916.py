# Generated by Django 2.2.7 on 2019-11-05 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_auto_20191104_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='expiration_date',
            field=models.DateField(),
        ),
    ]