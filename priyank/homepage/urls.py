from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('songs/', views.songs, name='songs'),
    path('videos/', views.videos, name='videos'),
    path('bookings/', views.bookings, name='bookings'),
    path('shop/', views.shop, name='shop'),
    path('subscribe/', views.subscribe, name='subscribe'),
]