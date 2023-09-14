from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'base/index.html')
def create(request):
    return render(request, 'base/create.html')

def update(request):
    context = {
        'title': 'Update',
        'content': 'Sarlavha',
        'id': 1,
        'name': 'Update',
        'email': '<EMAIL>',
        'password': '<PASSWORD>',
        'password2': '<PASSWORD>',
        'gender': 'Male',
        'age' : '<AGE>',
        'city' : '<CITY>',
        'country' : '<COUNTRY>',
    }
    return render(request, 'base/update.html', context)