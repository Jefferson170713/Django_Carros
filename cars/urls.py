from django.urls import path
from cars.views import cars_views

app_name = 'cars'

urlpatterns = [
    path('', cars_views, name='cars_views'),
]