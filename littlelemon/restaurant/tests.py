from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from django.contrib.auth.models import User

class MenuItemTestCase(TestCase):
    def test_get_item(self):
        menuItem = Menu(name='Milkshake', price=10.0, inventory=10)
        self.assertEqual(str(menuItem), 'Milkshake : 10.0')

class MenuItemsViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
        username='testuser',
        password='testpass'
    )
        Cheese = Menu.objects.create(name='Cheese', price=9.99, inventory=5)
        Fish = Menu.objects.create(name='Fish', price=5.50, inventory=10)
        
    # Menu.objects.create(name='Cheese', price=10.0, inventory=5)
    # Menu.objects.create(name='Fish', price=5.5, inventory=10)
    
    def test_menu_items_list(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('menu-items'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cheese')
        self.assertContains(response, 'Fish')
