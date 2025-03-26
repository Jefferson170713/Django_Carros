from django.shortcuts import render
from django.http import HttpResponse
import locale
from cars.models import Car
from cars.forms import CarForm

# Configura a localidade para o formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def format_float(value):
    return locale.format_string('%.2f', value, grouping=True)

def format_int(value):
    return locale.format_string('%.f', value, grouping=True)

# Create your views here.
def cars_views( request ):
    cars = Car.objects.all()
    search = request.GET.get('search', '').strip()

    if search:
        cars = cars.filter(model__icontains=search)
        print(cars)
    # formatando valores inteiros
    for car in cars:
        car.value = format_float(car.value)
    
    context = {
        'cars': cars,
        'search': search,
    }
    return render(
        request, 
        'cars/cars_index.html', 
        context,
    )

def new_car( request ):
    new_car_form = CarForm()
    context ={
        'new_car_form': new_car_form,
    }
    return render(
        request, 
        'cars/new_car.html',
        context,
    )