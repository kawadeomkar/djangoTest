from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SearchForm
from django.contrib.auth import authenticate, login
from .forms import UserForm
from .models import ParkingSpot


def home(request):
    return render(request, 'home/home.html', {'hi': 'hi'})


def signup(request):
    return render(request, 'home/signup.html', {'hi': 'hi'})


def search(request):
    spots = ParkingSpot.objects.all()
    city = request.GET['city']
    spots = spots.filter(city__icontains=city)
    if spots:
        response = "spots in " + city + ":<br>" + '<br>'.join([str(i) for i in spots])
    else:
        response = "no spots found sorry!!"
    return HttpResponse(response)
