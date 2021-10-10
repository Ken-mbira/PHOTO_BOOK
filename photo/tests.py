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

    def test_get_image_by_id(self):
        """This will test if one can get an image by the id
        """
        self.graduation.save_image()
        image = Image.get_image_by_id(1)
        self.assertEqual(image.pk,self.graduation.pk)

    def test_delete_image(self):
        """
        This will test that an image can be deleted from the database given its id"""
        self.graduation.save_image()
        self.graduation.delete_image()

        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        """This will test the method to update an image's records
        """
        self.graduation.save_image()
        new_image_record = Image(name = 'marriage', image_path="anotherlocation", date_taken = datetime.date(2000,4,10),descriptions = 'This is a picture taken during my graduation',category = self.category,location = self.location)
        self.graduation.update_image(new_image_record)

        self.assertEqual(self.graduation.name,'marriage')

    def test_get_image_by_category(self):
        """This will test the method to get the images by their category
        """
        self.location.save_location()
        self.category.save_category()
        self.graduation.save_image()

        images = Image.get_image_by_category(1)   

        self.assertEqual(images[0],self.graduation) 


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

    def test_delete_category(self):
        """This checks whether the delete category method works
        """
        self.category1.save_category()
        self.category1.delete_category()
        categories = Category.objects.all()

        self.assertTrue(len(categories) == 0)

    def test_update_category(self):
        """This will check whether the update categoru method works
        """
        self.category1.save_category()
        new_category = Category(name = 'Another',description = '')

        self.category1.update_category(new_category)

        self.assertTrue(self.category1.name == 'Another')

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

    def test_delete_location(self):
        """This checks whether the delete category method works
        """
        self.location.save_location()
        self.location.delete_location()
        locations = Category.objects.all()

        self.assertTrue(len(locations) == 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()