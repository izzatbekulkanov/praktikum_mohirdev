from django.urls import path
from .views import *



urlpatterns = [
    path('', abouts, name='abouts'),
    path('addabout/', about_add, name='addabout'),
    path('news/<uuid:id>', about, name='about'),

    

]
