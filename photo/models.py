from django.db import models

class Category(models.Model):
    """This defines the category table and all its contents and behaviours

    Args:
        models ([module]): [This is where we import the model functionality]
    """ 
    name = models.CharField(max_length=50)

class Location(models.Model):
    """This defines the location table and all its contents and behaviours

    Args:
        models ([module]): [This is where we import the model functionality]
    """ 
    name = models.CharField(max_length=50)

class Image(models.Model):
    """This defines the image table and all its contents and behaviours

    Args:
        models ([module]): [This is where we import the model functionality]
    """ 
    name = models.CharField(max_length=50)
    # image_path = models.TextField(upload_to = 'articles/')
    date_taken = models.DateTimeField()
    descriptions = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)