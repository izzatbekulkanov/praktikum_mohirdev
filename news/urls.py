from django.urls import path
from .views import *



urlpatterns = [
    path('news/',index),
    path('create/', create),

]
