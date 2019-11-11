from django.test import TestCase
from menu.models import Menu, Item, Ingredient
from django.utils import timezone
from django.contrib.auth.models import User


class IngredientModelTests(TestCase):
    """Test the Ingerdient model."""

    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(
            name='Mango',
        )

    def test_ingredient_name(self):
        """Test ingedient name is set correctly"""
        mango = Ingredient.objects.get(name='Mango')
        self.assertEqual(str(mango), 'Mango')


class ItemModelTests(TestCase):
    """Test the item model."""

    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(name='Mango')
        self.ingredient2 = Ingredient.objects.create(name='Banana')
        self.ingredient3 = Ingredient.objects.create(name='Honey')
        self.ingredient_list = Ingredient.objects.all()

        self.user = User.objects.create_user(
            username='chef101',
            email='test@test.com',
            password='testpass',
        )

        self.item1 = Item.objects.create(
            name='Mango and Banana Smoothie',
            description="Mango banana smoothie is a thick and creamy smoothie that is prepared by "
                        "combining world’s two best fruits, mango and banana.",
            chef=self.user,
            created_date=timezone.now(),
            standard=True,
        )
        self.item1.ingredients.set(self.ingredient_list)

    def test_item_creation(self):
        """Test item is setup correctly"""
        mango_banana = Item.objects.get(name='Mango and Banana Smoothie')

        self.assertEqual(str(mango_banana), 'Mango and Banana Smoothie')
        self.assertEqual(str(mango_banana.chef), 'chef101')
        self.assertEqual(str(mango_banana.description), "Mango banana smoothie is a thick and creamy smoothie "
                                                        "that is prepared by combining world’s two best fruits, "
                                                        "mango and banana.")
        # self.assertQuerysetEqual(str(mango_banana.ingredients.all()), Ingredient.objects.all())
