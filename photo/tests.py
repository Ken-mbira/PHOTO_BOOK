from django.test import TestCase

from .models import Category,Image,Location

class TestImage(TestCase):
    """This defines tests for the image behaviours

    Args:
        TestCase ([module]): [This is where we inherit the testing infrastructure]
    """
    def setUp(self):
        """This will run before every other test does"""
        self.graduation = Image(name = 'Graduation', image_path="location", date_taken = '20/01/2020',descriptions = 'This is a picture taken during my graduation')

    def test_instance(self):
        """This will check if an instance of the image class is being created
        """
        self.assertTrue(isinstance(self.graduation,Image))