from django.shortcuts import render
from .utils import get_weather
from .models import FavouriteCity

# Create your views here.

def home(request):
  weather_data=None

  if request.method=="POST":
    city=request.POST.get('city')
    weather_data=get_weather(city)
    

  return render(request, 'weatherapp/home.html', context={'weather_data': weather_data})




