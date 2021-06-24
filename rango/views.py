from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
# (request) is an argument.
    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'
    }
    return render(request, 'rango/index.html', context=context_dict)
    

def about(request):
    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'
    }
    return render(request, 'rango/about.html', context=context_dict)



