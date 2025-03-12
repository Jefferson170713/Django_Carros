from django.shortcuts import render
from django.http import HttpResponse
import locale

# Configura a localidade para o formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def format_float(value):
    return locale.format_string('%.2f', value, grouping=True)

def format_int(value):
    return locale.format_string('%.f', value, grouping=True)

# Create your views here.
def cars_views(request):
    car = {
        'model': 'Maverick',
        'id': format_int(1579),
        'description': 'Carro Esportivo - Lorem ipsum dolor sit, amet consectetur adipisicing elit.',
        'value': format_float(19854758.89),
    }
    return render(request, 'cars/cars_index.html', {'cars': car})