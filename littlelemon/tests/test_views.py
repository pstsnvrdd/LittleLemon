from django.test import TestCase
from restaurant.models import Menu

class MenuItemsViews(TestCase):
    def setUp(self):
        shakshuka = Menu.objects.create(dish='Grilled Cheese', price=9.99, inventory=5)
        Hummus = Menu.objects.create(dish='Fish and Chips', price=5.50, inventory=10)
    
    def test_menu_items_list(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Grilled Cheese')
        self.assertContains(response, 'Fish and Chips')