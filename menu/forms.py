from django import forms
from . import models
from . import validators

# Make a list of all items and their corresponding IDs
ITEMS = [[item.id, item.name] for item in models.Item.objects.all()]


class MenuForm(forms.ModelForm):
    """
    Form used to create new menus
    and edit existig menus.
    """

    # def __init__(self, *args, **kwargs):
    #     super(MenuForm, self).__init__(*args, **kwargs)
    #     self.fields['expiration_date'].validators.append(validators.validate_date)

    season = forms.CharField(
        required=True,
        error_messages={
            'required': "Season is required.",
        },
    ),
    items = forms.MultipleChoiceField(
        required=True,
        choices=ITEMS,
        label="Items - choose one or more from the list:",
        help_text='Hold down the Ctrl (windows) / Command (Mac) button to select multiple options.',
        error_messages={
            'required': "Choose at least one item.",
        }
    ),
    expiration_date = forms.DateField(
        required=True,
        error_messages={
            'invalid': "Enter a vaild date in the format 'YYYY-MM-DD'.",
            'required': "Expiration date is required.",
        },
        label="Expiration Date:",
        validators=[validators.validate_date]
    ),

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
        season = self.cleaned_data.get('season')
        items = self.cleaned_data.get('items')
        expiration_date = self.cleaned_data.get('expiration_date')

        print(season)
        print(items)
        print(expiration_date)

        if season != 'tree':
            msg = 'Season must be a tree!'
            self.add_error('season', msg)

        if 'Chocolate soda' not in items:
            msg = 'Menu must contain Chocolate soda!'
            self.add_error('items', msg)

        # validators.validate_date().validate(cleaned_data['expiration_date'])
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
