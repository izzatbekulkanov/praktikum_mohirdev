from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def abouts(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, "news/abouts.html",context)

def about(request,id):
    return render(request, "news/about.html")