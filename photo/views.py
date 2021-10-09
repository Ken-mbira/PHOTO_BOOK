import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .forms import ImageForm
from .models import Image
from django.core import serializers


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
    dataholder = serializers.serialize("json",images)
    data = json.dumps(dataholder)
    return render(request,'photohtml/images.html',{'images':images,"data":data})