from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('services', services, name='services'),
    path('brief', brief, name='brief'),
    path('jobs', jobs, name='jobs'),
    path('gallery', gallery, name='gallery')

]