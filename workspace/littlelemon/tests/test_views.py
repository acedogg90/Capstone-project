from django.test import TestCase
from restaurant.models import MenuItem, Booking
from restaurant.serializers import MenuItemSerializer  # Ensure you've imported this
from datetime import datetime, timedelta

class MenuViewTest(TestCase):
    @classmethod
    def setUp(self):
        self.menu_items = [
            MenuItem.objects.create(title="Pizza", price=12.99, inventory=10),
            MenuItem.objects.create(title="Burger", price=5.99, inventory=20),
            MenuItem.objects.create(title="Coke", price=1.99, inventory=100),
        ]

    def test_getall(self):
        
        response = self.client.get('/menu/items/')
        self.assertEqual(response.status_code, 200)

        serialized_data = MenuItemSerializer(self.menu_items, many=True).data
        self.assertEqual(serialized_data, response.data)  # Compare the serialized data

# class BookingViewTest(TestCase):
#     @classmethod
#     def setUp(self):
#         self.booking_tables = [
#             Booking.objects.create(name="John Doe", no_of_guests=12, booking_date="2023-10-31T16:00:00Z"),
#             Booking.objects.create(name="Burger", no_of_guests=5, booking_date="2023-11-31T16:00:00Z"),
#             Booking.objects.create(name="Coke", no_of_guests=1, booking_date="2023-12-30T16:00:00Z"),
#         ]

#     def test_getall(self):
        
#         response = self.client.get('/booking/tables/')
#         self.assertEqual(response.status_code, 200)

#         serialized_data = MenuItemSerializer(self.booking_tables, many=True).data
#         self.assertEqual(serialized_data, response.data)
        
class BookingModelTestCase(TestCase):

    def setUp(self):
        # This method is used to setup any data that is needed for the tests.
        # We'll create a booking instance here.
        Booking.objects.create(
            name="John Doe",
            no_of_guests=3,
            booking_date=datetime.now() + timedelta(days=7)  # booking for 7 days from now
        )

    def test_booking_creation(self):
        # Test that the booking was correctly created
        booking = Booking.objects.get(name="John Doe")
        self.assertEqual(booking.no_of_guests, 3)
        self.assertIsInstance(booking.booking_date, datetime)

    def test_str_representation(self):
        # Test the string representation of the booking
        booking = Booking.objects.get(name="John Doe")
        expected_str = f"Booking for {booking.name} on {booking.booking_date}"
        self.assertEqual(str(booking), expected_str)