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
        self.location = Location(name = 'Kiserian')
        self.location.save_location()

        self.category = Category(name = 'Cool')
        self.category.save_category()

        self.graduation = Image(name = 'Graduation', image_path="location", date_taken = datetime.date(2020,1,12),descriptions = 'This is a picture taken during my graduation',category = self.category,location = self.location)

    def test_instance(self):
        """This will check if an instance of the image class is being created
        """
        self.assertTrue(isinstance(self.graduation,Image))

    def test_save_image(self):
        """This checks if an image instance can be saved to the database
        """
        self.graduation.save_image()
        images = Image.objects.all()

        self.assertTrue(len(images)>0)

    def test_add_category(self):
        """This will check if a category has been added to an image instance
        """
        self.assertTrue(self.graduation.category == self.category)

    def test_add_location(self):
        """This will check if a location has been added to an image instance
        """
        self.assertTrue(self.graduation.location == self.location)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


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

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

class TestLocation(TestCase):
    """This defines tests for the behaviours of the location class

    Args:
        TestCase ([type]): [description]
    """
    def setUp(self):
        """This runs before all the tests do
        """
        self.location = Location(name = 'Kiserian')

    def test_instance(self):
        """This tests whether a created location is an instance of the location class
        """
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        """This checks if a location can be saved to the database
        """
        self.location.save_location()
        locations = Location.objects.all()

        self.assertTrue(len(locations) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()