from django import forms
from . import models

# Make a list of all items and their corresponding IDs
ITEMS = [[item.id, item.name] for item in models.Item.objects.all()]


class MenuForm(forms.ModelForm):
    season = forms.CharField(
        required=True,
        error_messages={
            'required': "Season is required.",
        },
    )
    expiration_date = forms.DateField(
        required=True,
        error_messages={
            'invalid': "Enter a vaild date in the format 'YYYY-MM-DD'.",
            'required': "Expiration date is required.",
        },
        label="Expiration Date:",
        help_text='hejh',
    )
    items = forms.MultipleChoiceField(
        required=True,
        # validators=
        choices=ITEMS,
        help_text='Hold down the Ctrl (windows) / Command (Mac) button to select multiple options.',
        error_messages={
            'required': "Choose at least one item.",
        },
    )

    class Meta:
        model = models.Menu
        fields = [
            'season',
            'items',
            'expiration_date',
        ]
