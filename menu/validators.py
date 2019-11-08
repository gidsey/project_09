"""Custom validators."""

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _

# Sample list of brnad names
BRANDS = ['coca-cola', 'pepsi', 'cola', 'coke', '7up', 'sprite', 'fanta', 'tab', 'mountain dew', 'dr pepper', 'tango.']


def BrandCheckValidator(value):
    """Validate the season does not contain any brand names."""
    if value.lower() in BRANDS:
        raise ValidationError(
            _('Season cannot contain any brand names!'),
            code='brandnames_not_allowed'
            )
