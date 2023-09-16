from django.urls import path
from .views import *



urlpatterns = [
    path('', abouts, name='abouts'),
    path('news/<uuid:id>', about, name='about'),
    

]
