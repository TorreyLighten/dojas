from django.shortcuts import render, redirect
from .models import *
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
    
def dojo(request):
    name = request.POST["name"]
    city = request.POST["city"]
    state = request.POST["state"]
    Dojo.objects.create(name = name, city = city, state = state)
    return redirect('/')

def ninja(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    dojo_location = request.POST["dojo_location"]
    Ninja.objects.create(first_name = first_name, last_name = last_name, dojo_location = dojo_location)
    return redirect('/')
