from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """This renders the home page
    """
    html = 'Hello World!'
    return HttpResponse(html)
