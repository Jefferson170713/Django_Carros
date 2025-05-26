from django.urls import path
from accounts.views import register_view
from accounts.views import login_view
from accounts.views import logout_view

app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
