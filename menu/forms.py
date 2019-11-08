from django import forms
from . import models
from . import validators

import datetime


# Make a list of all items and their corresponding IDs
ITEMS = [[item.id, item.name] for item in models.Item.objects.all()]


class MenuForm(forms.ModelForm):
    """
    Form used to create new menus
    and edit existig menus.
    """

    def __index__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['season'].validators.append(validators.BrandCheckValidator)

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
        choices=ITEMS,
        label="Items (choose one or more from the list):",
        help_text='Hold down the Ctrl (windows) / Command (Mac) button to select multiple options.',
        error_messages={
            'required': "Choose at least one item.",
        }
    )
    expiration_date = forms.DateField(
        required=True,
        error_messages={
            'invalid': "Enter a vaild date in the format 'YYYY-MM-DD'.",
            'required': "Expiration date is required.",
        },
        label="Expiration Date:",

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
        expiration_date = cleaned_data.get('expiration_date')

        if expiration_date < datetime.date.today():
            msg = 'Expiry date cannot be in the past.'
            self.add_error('expiration_date', msg)

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
