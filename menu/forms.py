from django import forms
# from django.forms.extras.widgets import SelectDateWidget

from .models import Menu, Item, Ingredient
from django.forms import DateField


class MenuForm(forms.ModelForm):

    expiration_date = DateField

    class Meta:
        model = Menu

        fields = (
            'expiration_date',
            'items',
        )
        exclude = ('created_date', )
