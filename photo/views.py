from django.shortcuts import render
from django.http import HttpResponse

from .forms import ImageForm


def index(request):
    """This renders the home page
    """
    return render(request,'photohtml/index.html') 

def images(request):
    """This will render the images page

    Args:
        request ([type]): [description]
    """
    return render(request,'photohtml/images.html')