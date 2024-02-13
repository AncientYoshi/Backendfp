from django.test import TestCase
from Restaurant.models import Menu  # Import the Menu model from your app

class MenuTest(TestCase):
    def test_menu_representation(self):
        # Create a new instance of the Menu model
        menu_item = Menu.objects.create(name="Noodle", price=5)

        # Assert that the string representation of the menu_item matches the anticipated value
        self.assertEqual(str(menu_item), "Noodle - $5")
