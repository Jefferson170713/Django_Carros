from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cars_views( request ):
    return render( request, 'cars/cars_index.html' )
