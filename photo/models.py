from django.db import models
from tk import Tk

class Category(models.Model):
    """This defines the category table and all its contents and behaviours

    Args:
        models ([module]): [This is where we import the model functionality]
    """ 
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def save_category(self):
        """This adds a category to the database
        """
        self.save()

    def delete_category(self):
        """This removes a category from the database
        """
        self.delete()

    def update_category(self,new):
        """This will update a category

        Args:
            new ([type]): [description]
        """
        self.name = new.name
        self.description = new.description
        self.save()

    def __str__(self):
        return self.name

class Location(models.Model):
    """This defines the location table and all its contents and behaviours

    Args:
        models ([module]): [This is where we import the model functionality]
    """ 
    name = models.CharField(max_length=50)

    def save_location(self):
        """This adds a location to the database
        """
        self.save()

    def delete_location(self):
        """This removes a location from the database
        """
        self.delete()

    def update_location(self,new):
        """This updates the content of the location
        """
        self.name = new.name
        self.save()

    def __str__(self):
        return self.name

class Image(models.Model):
    """This defines the image table and all its contents and behaviours

    Args:
        models ([module]): [This is where we import the model functionality]
    """ 
    name = models.CharField(max_length=50)
    image_path = models.ImageField(upload_to = 'articles/',blank=True)
    date_taken = models.DateField()
    descriptions = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        """This saves and image instance to the database
        """
        self.save()

    def get_image_by_id(id):
        image = Image.objects.get(pk = id)

        return image

    def delete_image(self):
        """This deletes the image from the database using its pk

        Args:
            id ([type]): [description]
        """
        self.delete()

    def update_image(self,new):
        """This method will update a record of an image
        """
        self.name = new.name
        self.image_path = new.image_path
        self.date_taken = new.date_taken
        self.descriptions = new.descriptions
        self.category = new.category
        self.location = new.location
        self.save()

    def get_image_by_category(pk):
        """This method will return all the images that fall in a described category
        """
        images = Image.objects.filter(category__pk = pk)
        return images

    @classmethod
    def get_image_by_name(cls,search_term):
        """This will return images provided they match the criteria provided in the search term

        Args:
            search_term ([type]): [description]
        """
        images = cls.objects.filter(name__icontains = search_term)
        return images
        

