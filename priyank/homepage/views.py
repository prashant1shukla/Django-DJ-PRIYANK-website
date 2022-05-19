from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def songs(request):
    return render(request, 'songs.html')

def videos(request):
    return render(request, 'videos.html')

def bookings(request):
    return render(request, 'bookings.html')
    
def shop(request):
    return render(request, 'shop.html')

def subscribe(request):
    return render(request, 'subscirbe.html')