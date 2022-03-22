from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def world(request):
    return render(request, "world.html")

def asia(request):
    return render(request, "asia.html")

def malaysia(request):
    return render(request, "malaysia.html")
