from django import forms

from .models import Menu, Item
# from django.forms import DateField, CharField, MultipleChoiceField


TEST_CHOICES = [[x.id, x.name] for x in Item.objects.all()]
# TEST_CHOICES = [[x.id, x.item] for x in Menu.objects.all().filter(items__items__isnull=False)]

# TEST_CHOICES =[[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd']]


class MenuForm(forms.ModelForm):
    season = forms.CharField
    expiration_date = forms.DateField

    items = forms.MultipleChoiceField(
        # validators=
        choices=TEST_CHOICES,
        help_text='Hold down the Ctrl (windows) / Command (Mac) button to select multiple options.',
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Menu

        fields = (
            'season',
            'items',
            'expiration_date',
        )
        # exclude = ('created_date', )
