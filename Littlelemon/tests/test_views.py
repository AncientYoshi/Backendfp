from django.test import TestCase
from django.urls import reverse
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few instances of the Menu model for testing
        self.menu_item1 = Menu.objects.create(name="Noodle", price=5.00)
        self.menu_item2 = Menu.objects.create(name="Chocolate", price=2.00)

    def test_getall(self):
        # Make a GET request to the API endpoint that retrieves all Menu items
        client = APIClient()
        url = reverse('menu-list')  # Assuming your API endpoint is named 'menu-list'
        response = client.get(url)

        # Serialize the retrieved data
        expected_data = MenuSerializer([self.menu_item1, self.menu_item2], many=True).data

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if the serialized data matches the response data
        self.assertEqual(response.data, expected_data)
