import re
from django.shortcuts import render, HttpResponse
#from .task1 import checkbits
from home import task1


# Create your views here.

def index(request,a,b):
    dict = task1.checkbits(a,b)
    return HttpResponse("<h1> The dictionary is %s</h1>" % dict)   
def checkbits(request):
    return HttpResponse("this is homepage")
