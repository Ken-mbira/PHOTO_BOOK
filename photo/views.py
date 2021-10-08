from django.shortcuts import render
from django.http import HttpResponse

from .forms import ImageForm
from .models import Image


def index(request):
    """This renders the home page
    """
    return render(request,'photohtml/index.html') 

def images(request):
    """This will render the images page

    Args:
        request ([type]): [description]
    """
    images = Image.objects.all()
    image1 = Image.objects.first()
    return render(request,'photohtml/images.html',{'images':images,"image1":image1})