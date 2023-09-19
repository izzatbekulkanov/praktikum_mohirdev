from django.shortcuts import render
from django.http import HttpResponse
from news.models import *
from django.shortcuts import redirect
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

# detail page
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
def about_add(request):
    if request.method == 'POST':
        form = AddAboutForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('abouts')
            # Boshqa ma'lumotlarga yo'naltirish
    else:
        form = AddAboutForm()

    context = {
        'form': form,
    }
    return render(request, "news/about_edit.html", context)
def about_edit(request, id):
    project = Project.objects.get(id=id)
    form = AddAboutForm(instance=project)
    if request.method == 'POST':
        form = AddAboutForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('abouts')
            # Boshqa ma'lumotlarga yo'naltirish


    context = {
        'form': form,
    }
    return render(request, "news/about_edit.html", context)
def about_delete(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('abouts')