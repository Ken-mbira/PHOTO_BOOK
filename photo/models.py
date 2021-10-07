from django.db import models

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
