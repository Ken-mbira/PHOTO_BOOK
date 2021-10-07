from django.test import TestCase
import datetime

from .models import Category,Image,Location

class TestImage(TestCase):
    """This defines tests for the image behaviours

    Args:
        TestCase ([module]): [This is where we inherit the testing infrastructure]
    """
    def setUp(self):
        """This will run before every other test does"""
        self.graduation = Image(name = 'Graduation', image_path="location", date_taken = datetime.date(2020,1,12),descriptions = 'This is a picture taken during my graduation')

    def test_instance(self):
        """This will check if an instance of the image class is being created
        """
        self.assertTrue(isinstance(self.graduation,Image))

    # def test_save_image(self):
    #     """This tests whether an image can be saved to the database
    #     """
    #     self.graduation.save_image()
    #     images = Image.objects.all()
    #     self.AssertTrue(len(images) > 1)


class TestCategory(TestCase):
    """This defines tests for all behaviours of the Category class

    Args:
        TestCase ([type]): [description]
    """
    def setUp(self):
        """This will run before every test does
        """
        self.category1 = Category(name = 'mycategory',description = 'This is my category')

    def test_category_instance(self):
        """This will test if the the category is an instance of the category class
        """
        self.assertTrue(isinstance(self.category1,Category))

    def test_save_category(self):
        """This tests whether a new category can be saved to the database
        """
        self.category1.save_category()
        categories = Category.objects.all()

        self.assertTrue(len(categories) > 0)