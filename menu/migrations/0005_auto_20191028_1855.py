# Generated by Django 2.2.6 on 2019-10-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20191025_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
