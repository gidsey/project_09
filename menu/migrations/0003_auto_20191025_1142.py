# Generated by Django 2.2.6 on 2019-10-25 10:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20160406_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='expiration_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 24, 10, 42, 20, 683796, tzinfo=utc)),
            preserve_default=False,
        ),
    ]