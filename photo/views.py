from django.shortcuts import render
from django.http import HttpResponse

from .forms import ImageForm


def index(request):
    """This renders the home page
    """
    form = ImageForm
    return render(request,'photohtml/index.html',{'form':form}) 
