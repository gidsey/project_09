from django import forms
from .models import Menu, Item


ITEMS = [[x.id, x.name] for x in Item.objects.all()]  # Make a list of all items and their corresponding IDs


class MenuForm(forms.ModelForm):
    season = forms.CharField
    expiration_date = forms.DateField
    items = forms.MultipleChoiceField(
        # validators=
        choices=ITEMS,
        help_text='Hold down the Ctrl (windows) / Command (Mac) button to select multiple options.',
        # initial=[2, 4, 6]
    )

    class Meta:
        model = Menu

        fields = (
            'season',
            'items',
            'expiration_date',
        )
