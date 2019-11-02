from django import forms
from . import models

# Make a list of all items and their corresponding IDs
ITEMS = [[item.id, item.name] for item in models.Item.objects.all()]


class MenuForm(forms.ModelForm):
    season = forms.CharField
    expiration_date = forms.DateField
    items = forms.MultipleChoiceField(
        # validators=
        choices=ITEMS,
        help_text='Hold down the Ctrl (windows) / Command (Mac) button to select multiple options.',
    )

    class Meta:
        model = models.Menu
        fields = [
            'season',
            'items',
            'expiration_date',
        ]
