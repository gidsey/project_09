"""Custom validators."""
import datetime
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _

# Sample list of brnad names
BRANDS = ['coca-cola', 'pepsi', 'coca', 'cola', 'coke', '7up', 'sprite', 'fanta', 'tab',
          'mountain dew', 'dr pepper', 'tango', ]


def BrandCheckValidator(value):
    """Ensure season does not contain any brand names."""
    word_list = re.sub(r'[^\w]', ' ', value).split()
    for word in word_list:
        if word.lower() in BRANDS:
            raise ValidationError(
                _('Season cannot contain any brand names!'),
                code='brandnames_not_allowed'
            )


def PastDateValidator(exp_date):
    """Check that the expiry date is not in the past."""
    if exp_date < datetime.date.today():
        raise ValidationError(
            _('Expiry date cannot be in the past.'),
            code='expiry_date_in_past'
        )
