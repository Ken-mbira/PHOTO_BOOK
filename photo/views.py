import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .forms import ImageForm
from .models import Image,Category
from django.core import serializers


def index(request):
    """This renders the home page
    """
    categories = Category.objects.all()
    return render(request,'photohtml/index.html',{"categories":categories})

def images(request):
    """This will render the images page

    Args:
        request ([type]): [description]
    """
    categories = Category.objects.all()
    images = Image.objects.all()
    return render(request,'photohtml/images.html',{'images':images,"categories":categories})

def image_spec(request,pk):
    """This will render the page containing a specific image

    Args:
        request ([type]): [description]
        pk ([int]): [This is the primary key of the image]
    """
    categories = Category.objects.all()
    image = Image.get_image_by_id(pk)
    return render(request,"photohtml/image.html",{"image":image,"categories":categories})

def image_category(request,pk):
    """This will render a page containing the specific category asked for

    Args:
        request ([type]): [description]
        pk ([type]): [description]
    """
    categories = Category.objects.all()
    images = Image.get_image_by_category(pk)

    return render(request,'photohtml/image_category.html',{"images":images,"categories":categories})