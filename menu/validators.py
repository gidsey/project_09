"""Custom validators."""

from django.core.exceptions import ValidationError


BRANDS = ['coca-cola', 'pepsi', 'coke', '7up']


class BrandCheckValidator:
    """Validate the seaon does not contain any brand names."""
    def validate(self, season):
        if season in BRANDS:
            raise ValidationError(
                "Season cannot contain any brand names!",
                code='season_contains_brandnames'
                )
