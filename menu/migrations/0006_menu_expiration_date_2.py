# Generated by Django 2.2.6 on 2019-10-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20191028_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='expiration_date_2',
            field=models.DateField(blank=True, null=True),
        ),
    ]
