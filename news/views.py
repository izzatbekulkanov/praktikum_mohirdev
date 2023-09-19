from django.shortcuts import render
from django.http import HttpResponse
from news.models import *
from .forms import AddAboutForm

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
    }
    return render(request, "news/about.html", context)


def about_add(request):
    if request.method == 'POST':
        form = AddAboutForm(request.POST)
        if form.is_valid():
            form.save()
            # Boshqa ma'lumotlarga yo'naltirish
    else:
        form = AddAboutForm()

    context = {
        'form': form,
    }
    return render(request, "news/about_add.html", context)