"""Custom validators."""

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _

BRANDS = ['coca-cola', 'pepsi', 'coke', '7up']


class BrandCheckValidator:
    """Validate the seaon does not contain any brand names."""
    def validate(self, season):
        if season in BRANDS:
            raise ValidationError(
                _("Season cannot contain any brand names!"),
                code='season_contains_brandnames'
                )


def validate_date(value):
    print('validate_date called')
    print(value)
