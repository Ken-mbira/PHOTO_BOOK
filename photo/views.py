from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """This renders the home page
    """
    return render(request,'photohtml/index.html') 
