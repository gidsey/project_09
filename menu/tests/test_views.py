from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase

from menu.models import Menu, Item, Ingredient
from menu import views

from django.utils import timezone
import datetime


class MenuViewsTests(TestCase):
    """Test the views."""
    pass
    # def setUp(self):
    #     #  Every test needs access to the request factory.
    #     self.factory = RequestFactory()
    #     self.ingredient1 = Ingredient.objects.create(
    #         name='Mango',
    #     )
    #     self.ingredient2 = Ingredient.objects.create(
    #         name='Banana',
    #     )
    #     self.ingredient3 = Ingredient.objects.create(
    #         name='Honey',
    #     )
    #     self.item1 = Item.objects.create(
    #         name='Mango and Banana Smoothie',
    #         description="Mango banana smoothie is a thick and creamy smoothie that is prepared by "
    #                     "combining world’s two best fruits, mango and banana.",
    #         chef='',
    #         created_date=timezone.now(),
    #         standard=True,
    #         ingredients='',
    #     )
    #     self.menu1 = Menu.objects.create(
    #         season='Autumn 2019',
    #         item='',
    #         created_date=timezone.now(),
    #         expiration_date=datetime.date.today() + datetime.timedelta(days=14)
    #     )
    #
    # def test_check_data_view(self):
    #     """Check the index page is redirecting if DB contains data"""
    #     request = self.factory.get('/')
    #     response = views.menu_list(request)
    #     self.assertEqual(response.status_code, 200)