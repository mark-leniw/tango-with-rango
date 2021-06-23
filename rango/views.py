from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
# (request) is an argument.
    return HttpResponse("Rango says hey there partner!")
    # HttpResponse in an object from the django.http module
    


