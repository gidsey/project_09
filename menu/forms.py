from django import forms
from . import models
from . import validators

import datetime


# Make a list of all items and their corresponding IDs
# ITEMS = [[item.id, item.name] for item in models.Item.objects.all()]


class MenuForm(forms.ModelForm):
    """
    Form used to create new menus
    and edit existig menus.
    """

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['season'].validators.append(validators.BrandCheckValidator)
        self.fields['expiration_date'].validators.append(validators.PastDateValidator)
        self.fields['items'].choices = choices



    season = forms.CharField(
        required=True,
        label='Season (no brand names please):',
        error_messages={
            'required': "Season is required.",
        },
        validators=[validators.BrandCheckValidator]
    )
    items = forms.MultipleChoiceField(
        required=True,
        # choices=ITEMS,
        label="Items (choose two or more from the list):",
        help_text='Hold down the Ctrl (windows) / Command (Mac) button to select multiple options.',
        error_messages={
            'required': "Choose at least two items.",
        }
    )
    expiration_date = forms.DateField(
        required=True,
        error_messages={
            'invalid': "Enter a vaild date in the format 'YYYY-MM-DD'.",
            'required': "Expiration date is required.",
        },
        label="Expiration Date:",
        validators=[validators.PastDateValidator]
    )

    class Meta:
        model = models.Menu
        fields = [
            'season',
            'items',
            'expiration_date',
        ]

    def clean(self):
        """Validate the form input."""
        cleaned_data = super(MenuForm, self).clean()
        items = cleaned_data.get('items')

        if items:
            if len(items) < 2:
                msg = 'You must pick at least two items.'
                self.add_error('items', msg)

        return cleaned_data


class DeleteMenuForm(forms.ModelForm):
    """
    Form used to delete menus.
    """
    season = forms.CharField(required=True)
    expiration_date = forms.DateField(required=True)

    class Meta:
        model = models.Menu
        fields = [
            'season',
            'expiration_date',
        ]
