from django.shortcuts import render
from django.http import HttpResponse
# from django.template import Context, loader


# Create your views here.
def django(request):
    return render(request, "django.html")

def affichage(request):
    return render(request, "affichage.html")

def templates(request):
    return render(request, "templates.html")