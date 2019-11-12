from django.contrib.sessions.middleware import SessionMiddleware
import datetime
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q

from menu.models import Menu, Item, Ingredient
from menu import views

class MenuViewsTests(TestCase):
    """Test the views."""
    def setUp(self):

        #  Every test needs access to the request factory.
        self.factory = RequestFactory()

        #  Create a user
        self.user = User.objects.create_user(username='Jamie Oliver', email='test@test.com', password='testpass')
        #  Create 3x ingredients
        self.ingredient1 = Ingredient.objects.create(name='Mango')
        self.ingredient2 = Ingredient.objects.create(name='Banana')
        self.ingredient3 = Ingredient.objects.create(name='Honey')
        #  Create two sets of ingredients
        self.all_ingredients = Ingredient.objects.all()
        self.two_ingredients = Ingredient.objects.filter(
            Q(name__iexact='Banana') | Q(name__iexact='Honey')).order_by('name')
        #  Create 2x items
        self.item1 = Item.objects.create(
            name='Mango and Banana Smoothie',
            description="Mango banana smoothie is a thick and creamy smoothie.",
            chef=self.user,
            created_date=timezone.now(),
            standard=True,
        )
        self.item1.ingredients.set(self.all_ingredients)
        self.item2 = Item.objects.create(
            name='Banana and Honey Smoothie',
            description="A delicious banana and honey drink.",
            chef=self.user,
            created_date=timezone.now(),
            standard=False,
        )
        self.item2.ingredients.set(self.two_ingredients)
        self.all_items = Item.objects.all()
        #  Create a menu
        self.menu1 = Menu.objects.create(
            season='Autumn 2019',
            created_date=timezone.now(),
            expiration_date=timezone.now() + datetime.timedelta(days=14)
        )
        self.menu1.items.set(self.all_items)

    def test_menu_list_view(self):
        """Check the index page view"""
        request = self.factory.get('/')
        response = views.menu_list(request)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.menu1.season)
        self.assertContains(response, self.menu1.expiration_date.strftime("%b. %d, %Y"))
        for item in self.menu1.items.all():
            self.assertContains(response, item)

    def test_menu_detail_view(self):
        """Check the menu detail view."""
        request = self.factory.get('/menu/')
        response = views.menu_detail(request, **{'pk': self.menu1.pk})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.menu1.season)
        self.assertContains(response, self.menu1.expiration_date.strftime("%B %d, %Y"))
        for item in self.menu1.items.all():
            self.assertContains(response, item)

    def test_item_detail_view(self):
        """Check the menu detail view."""
        request = self.factory.get('/menu/item/')
        response = views.item_detail(request, **{'pk': self.item1.pk})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item1)
        self.assertContains(response, self.item1.chef)
        for ingredient in self.item1.ingredients.all():
            self.assertContains(response, ingredient)