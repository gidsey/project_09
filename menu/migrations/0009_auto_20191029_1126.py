# Generated by Django 2.2.6 on 2019-10-29 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20191029_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='expiration_date_2',
            new_name='expiration_date',
        ),
    ]
