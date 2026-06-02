from django.test import TestCase
from restaurant.models import Menu

class MenuItemTestCase(TestCase):
    def test_get_item(self):
        menuItem = Menu(dish='Milkshake', price=10.00, inventory=10)
        self.assertEqual(str(menuItem), 'Milkshake : 10.00')