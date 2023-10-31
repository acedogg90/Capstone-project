from django.test import TestCase
from restaurant.models import MenuItem

class MenuTest(TestCase):
    # Define an instance method that adds a new instance of the MenuItem model. 
    def test_get_item(self):
        item = MenuItem.objects.create(title="Pizza", price=12.99, inventory=10)
        # Call the assertEqual() method of the test class that compares the string representation of the newly added object with the anticipated value.
        self.assertEqual(str(item), "Pizza : 12.99")
    
