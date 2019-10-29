# Generated by Django 2.2.6 on 2019-10-29 10:30
from datetime import date
from django.db import migrations

def populate_expiration_date_2(apps, schema_editor):
    """
    Convert DateTime data from expiration_date to Date format
    and save into temp field expiration-date_2
    """
    menu = apps.get_model('menu', 'Menu')

    menu_data = menu.objects.all()
    for item in menu_data:
        if item.expiration_date:
            item.expiration_date_2 = date(item.expiration_date)
            menu.save()


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_menu_expiration_date_2'),
    ]

    operations = [
    ]
