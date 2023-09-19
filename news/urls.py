from django.urls import path
from .views import *



urlpatterns = [
    path('', abouts, name='abouts'),
    path('addabout/', about_add, name='addabout'),
    path('deleteabout/<uuid:id>', about_delete, name='deleteabout'),
    path('editabout/<uuid:id>', about_edit, name='editabout'),
    path('news/<uuid:id>', about, name='about'),

]
