from django import forms

from .models import Menu
from django.forms import DateField, CharField


class MenuForm(forms.ModelForm):
    season = CharField
    expiration_date = DateField

    class Meta:
        model = Menu

        fields = (
            'season',
            'items',
            'expiration_date',
        )
        exclude = ('created_date', )
