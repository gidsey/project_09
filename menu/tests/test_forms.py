from django.test import TestCase
from menu.forms import MenuForm
import datetime

PLUS_TWO_WEEKS = datetime.date.today() + datetime.timedelta(days=14)
MINUS_TWO_WEEKS = datetime.date.today() - datetime.timedelta(days=14)


class MenuFormTests(TestCase):
    """
    Test menu creation and editing
    via the MenuForm with both
    valid and invalid data.
    """

    def test_menu_form_valid(self):
        """Form with valid data input"""
        form_data = ({
            'season': 'Spring/Summer',
            'items': [2, 3],
            'expiration_date': PLUS_TWO_WEEKS
        })
        form = MenuForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_menu_form_invalid_season_missing(self):
        """Form with no season input"""
        form_data = ({
            'season': '',
            'items': [2, 3],
            'expiration_date': PLUS_TWO_WEEKS
        })
        form = MenuForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_menu_form_invalid_season_too_long(self):
        """Form with no season > chars."""
        form_data = ({
            'season': 'Spring/Summer Spring/Summer Spring/Summer Spring/Summer Spring/Summer',
            'items': [2, 3],
            'expiration_date': PLUS_TWO_WEEKS
        })
        form = MenuForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_menu_form_invalid_season_contains_brandname(self):
        """Form with no season > chars."""
        form_data = ({
            'season': 'Spring with Coca-Cola',
            'items': [2, 3],
            'expiration_date': PLUS_TWO_WEEKS
        })
        form = MenuForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_menu_form_invalid_no_items(self):
        """Form with no items selcetd."""
        form_data = ({
            'season': 'Spring/Summer',
            'items': [],
            'expiration_date': PLUS_TWO_WEEKS
        })
        form = MenuForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_menu_form_invalid_one_items(self):
        """Form with only one item selcetd."""
        form_data = ({
            'season': 'Spring/Summer',
            'items': [2, ],
            'expiration_date': PLUS_TWO_WEEKS
        })
        form = MenuForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_menu_form_no_exp_date_set(self):
        """Form with no expiration date set."""
        form_data = ({
            'season': 'Spring/Summer',
            'items': [2, 4],
            'expiration_date': ''
        })
        form = MenuForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_menu_form_exp_date_in_past(self):
        """Form with  expiration date set in the past."""
        form_data = ({
            'season': 'Spring/Summer',
            'items': [2, 4],
            'expiration_date': MINUS_TWO_WEEKS
        })
        form = MenuForm(data=form_data)
        self.assertFalse(form.is_valid())