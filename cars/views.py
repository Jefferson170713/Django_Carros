from django.shortcuts import render
from django.http import HttpResponse
import locale
from cars.models import Car

# Configura a localidade para o formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def format_float(value):
    return locale.format_string('%.2f', value, grouping=True)

def format_int(value):
    return locale.format_string('%.f', value, grouping=True)

# Create your views here.
def cars_views(request):
    cars = Car.objects.all()
    # formatando valores inteiros
    for car in cars:
        car.value = format_float(car.value)
    
    return render(
        request, 
        'cars/cars_index.html', 
        {'cars': cars}
    )