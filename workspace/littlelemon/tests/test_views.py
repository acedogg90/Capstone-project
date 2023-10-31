from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer  # Ensure you've imported this

class MenuViewTest(TestCase):
    @classmethod
    def setUp(self):
        self.menu_items = [
            MenuItem.objects.create(title="Pizza", price=12.99, inventory=10),
            MenuItem.objects.create(title="Burger", price=5.99, inventory=20),
            MenuItem.objects.create(title="Coke", price=1.99, inventory=100),
        ]

    def test_getall(self):
        
        response = self.client.get('/restaurant/menu/items/')
        self.assertEqual(response.status_code, 200)

        serialized_data = MenuItemSerializer(self.menu_items, many=True).data
        self.assertEqual(serialized_data, response.data)  # Compare the serialized data
