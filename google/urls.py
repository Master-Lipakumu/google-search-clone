
from django.urls import path, include

from .views import index, search

app_name = 'google'

urlpatterns = [
    
    path('', index, name='index'),
    path('search/', search, name='search'),
]
