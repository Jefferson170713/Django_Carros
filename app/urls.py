from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_views
from accounts.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('accounts.urls')),
    #path('cars/', include('cars.urls')),
    path('', include('cars.urls')), # aqui é minha raiz do projeto, então não preciso colocar /cars/ na url
] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
