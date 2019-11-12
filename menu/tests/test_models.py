import datetime

from django.test import TestCase
from menu.models import Menu, Item, Ingredient
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q


class MenuModelTests(TestCase):
    """
    Test each related model in the Menu app:
    - Ingedient
    - Item
    - Menu
    """
    def setUp(self):
        #  Create a user
        self.user = User.objects.create_user(username='headchef', email='test@test.com', password='testpass')
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

    def test_ingredient_model(self):
        """Test ingedient name is set correctly"""
        mango = Ingredient.objects.get(name='Mango')
        self.assertEqual(str(mango), 'Mango')

    def test_item_model(self):
        """Test all fields on item."""
        mango_banana = Item.objects.get(name='Mango and Banana Smoothie')
        self.assertEqual(str(mango_banana), 'Mango and Banana Smoothie')
        self.assertEqual(str(mango_banana.chef), 'headchef')
        self.assertIn(str(mango_banana.description), "Mango banana smoothie is a thick and creamy smoothie.")
        self.assertGreater(timezone.now(), mango_banana.created_date)
        for ingredient in mango_banana.ingredients.all():
            self.assertIn(ingredient, self.all_ingredients)

        banana_honey = Item.objects.get(name='Banana and Honey Smoothie')
        banana_honey_ingredients = banana_honey.ingredients.all().order_by('name')
        # self.assertQuerysetEqual(banana_honey_ingredients, self.two_ingredients)
        self.assertEqual(len(banana_honey_ingredients), 2)

    def test_menu_model(self):
        """Test all fields on menu."""
        autumn_menu = Menu.objects.get(season='Autumn 2019')
        self.assertEqual(str(autumn_menu.season), 'Autumn 2019')
        self.assertGreater(timezone.now(), autumn_menu.created_date)
        self.assertLess(datetime.date.today(), autumn_menu.expiration_date)
        autumn_menu_items = autumn_menu.items.all().order_by('name')
        print('autumn_menu_items: {}'.format(autumn_menu_items))
        print('self.all_items:    {}'.format(self.all_items.order_by('name')))
        # self.assertQuerysetEqual(autumn_menu_items, self.all_items.order_by('name'))
        self.assertEqual(len(autumn_menu_items), 2)