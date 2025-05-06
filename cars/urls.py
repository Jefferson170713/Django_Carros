from django.urls import path
from cars.views import cars_views, new_car
#from django.conf import settings
#from django.conf.urls.static import static

app_name = 'cars'

urlpatterns = [
    path('cars/', cars_views, name='cars_index'),
    path('new_car/', new_car, name='new_car'),
] #+ static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )