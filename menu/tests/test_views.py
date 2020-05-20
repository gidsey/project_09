import datetime
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User, AnonymousUser
from django.utils import timezone
from django.db.models import Q

from menu.models import Menu, Item, Ingredient
from menu import views
from django.urls import reverse
from django.test import Client

PLUS_TWO_WEEKS = datetime.date.today() + datetime.timedelta(days=14)


class MenuViewsTests(TestCase):
    """Test the views."""
    def setUp(self):

        #  Every test needs access to the request factory.
        self.factory = RequestFactory()

        #  Create a user
        self.user = User.objects.create_user(
            username='Jamie Oliver',
            email='test@test.com',
            password='testpass')
        self.anonymous_user = AnonymousUser()

        #  Create 3x ingredients
        self.ingredient1 = Ingredient.objects.create(name='Mango')
        self.ingredient2 = Ingredient.objects.create(name='Banana')
        self.ingredient3 = Ingredient.objects.create(name='Honey')
        #  Create two QuerySets of ingredients
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
        #  Create a menu
        self.menu1 = Menu.objects.create(
            season='Autumn 2019',
            created_date=timezone.now(),
            expiration_date=timezone.now() + datetime.timedelta(days=14)
        )
        self.all_items = Item.objects.all().order_by('name')
        self.menu1.items.set(self.all_items)

        self.client = Client(enforce_csrf_checks=False)
        self.client.login(username='Jamie Oliver', password='testpass')

        #  define form fields/values
        self.menu_form_post_data_fail = {
            'season': 'All-new season',
            'items': ['1', '2'],
            'expiration_date': 'November 12, 2022',
        }

        self.menu_form_post_data_fail_2 = {
            'season': 'All-new season',
            'items': ['1'],
            'expiration_date': PLUS_TWO_WEEKS,
        }

        self.menu_form_post_data_pass = {
            'season': 'All-new season',
            'items': ['1', '2'],
            'expiration_date': PLUS_TWO_WEEKS,
        }

        self.menu_form_post_data_delete = {
            'season': self.menu1,
            'expiration_date': self.menu1.expiration_date.date(),
        }

    def test_menu_list_view(self):
        """Test the index page view"""
        request = self.factory.get('/')
        response = views.menu_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.menu1)
        # self.assertContains(response, self.menu1.expiration_date.strftime("%b %d, %Y"))
        for item in self.menu1.items.all():
            self.assertContains(response, item)

    def test_menu_detail_view(self):
        """Test the menu detail view."""
        request = self.factory.get('/menu/')
        response = views.menu_detail(request, **{'pk': self.menu1.pk})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.menu1.season)
        self.assertContains(response, self.menu1.expiration_date.strftime("%B %d, %Y"))
        for item in self.menu1.items.all():
            self.assertContains(response, item)

    def test_item_detail_view(self):
        """Test the menu detail view."""
        request = self.factory.get('/menu/item/')
        response = views.item_detail(request, **{'pk': self.item1.pk})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item1)
        self.assertContains(response, self.item1.chef)
        for ingredient in self.item1.ingredients.all():
            self.assertContains(response, ingredient)

    def test_create_new_menu(self):
        """
        Test the Create new menu view.
        Only accessible to logged in user.
        """
        request = self.factory.get('/menu/new/')
        request.user = self.user
        response = views.create_new_menu(request)
        self.assertEqual(response.status_code, 200)
        for item in self.all_items:
            self.assertContains(response, item)

    def test_edit_menu_get(self):
        """Test the edit menu view with a logged-in user."""
        request = self.factory.get('/menu/edit/')
        request.user = self.user
        response = views.edit_menu(request, **{'pk': self.menu1.pk})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.menu1)
        self.assertContains(response, self.menu1.expiration_date.date())
        for item in self.all_items:
            self.assertContains(response, item)

    def test_edit_menu_post_fail(self):
        """Test the resposnse when the edit menu form is posted with an invalid date."""
        form_addr = reverse('menu:menu_edit', kwargs={'pk': self.menu1.pk})
        response = self.client.post(form_addr,
                                    self.menu_form_post_data_fail,
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a vaild date")

    def test_edit_menu_post_pass(self):
        """Test the resposnse when the edit menu form is correctly posted."""
        form_addr = reverse('menu:menu_edit', kwargs={'pk': self.menu1.pk})
        response = self.client.post(form_addr,
                                    self.menu_form_post_data_pass,
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Menu updated successfully.")

    def test_create_new_menu_post_fail(self):
        """Test the resposnse when the new menu form is posted with on;y one item."""
        form_addr = reverse('menu:menu_new')
        response = self.client.post(form_addr,
                                    self.menu_form_post_data_fail_2,
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You must pick at least two items.")

    def test_create_new_menu_post_pass(self):
        """Test the resposnse when the new menu form is correctly posted."""
        form_addr = reverse('menu:menu_new')
        response = self.client.post(form_addr,
                                    self.menu_form_post_data_pass,
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Menu added successfully.")

    def test_edit_menu_anonymous(self):
        """Test the edit menu view with an anonymous user."""
        request = self.factory.get('/menu/edit/')
        request.user = self.anonymous_user
        response = views.edit_menu(request, **{'pk': self.menu1.pk})
        self.assertNotEqual(response.status_code, 200)

    def test_delete_menu_post_pass(self):
        """Test the resposnse when the delete menu form is correctly posted."""
        form_addr = reverse('menu:menu_delete', kwargs={'pk': self.menu1.pk})

        response = self.client.post(
                                    form_addr,
                                    self.menu_form_post_data_delete,
                                    follow=True
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Menu deleted successfully.")






