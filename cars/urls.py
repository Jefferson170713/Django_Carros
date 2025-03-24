from django.urls import path
from cars.views import cars_views
#from django.conf import settings
#from django.conf.urls.static import static

app_name = 'cars'

urlpatterns = [
    path('', cars_views, name='cars_views'),
] #+ static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )