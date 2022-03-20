from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("World Population")

def asia(request):
    return HttpResponse("Asia Population")

def malaysia(request):
    return HttpResponse("Malaysia Population")
