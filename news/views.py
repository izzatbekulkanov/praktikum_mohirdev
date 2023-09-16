from django.shortcuts import render
from django.http import HttpResponse
from news.models import *

# Create your views here.

def abouts(request):
    reviews_p = Review.objects.filter(value='+')
    reviews_m = Review.objects.filter(value='-')
    projects = Project.objects.filter(project_review__isnull=True)
    context = {
        'projects': projects,
        'reviews_m': reviews_m,
        'reviews_p': reviews_p,
    }
    return render(request, "news/abouts.html", context)

def about(request,id):
    project = Project.objects.get(id=id)
    context = {
        'project': project,
        'tags': tags
    }
    return render(request, "news/about.html", context)
