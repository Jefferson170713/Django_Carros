from django.contrib import admin
from cars.models import Car, Brand

# criando a 2° classe Brand
class BrandAdmin( admin.ModelAdmin ):
    list_display = ( 'name', 'id', )
    search_fields = ( 'name', )

# Criando a 1° classe CarAdmin 
class CarAdmin( admin.ModelAdmin ):
    list_display = ( 'model', 'brand', 'factory_year', 'model_year', 'value', )
    search_fields = ( 'model', 'brand__name', )

admin.site.register( Car, CarAdmin )
admin.site.register( Brand, BrandAdmin )