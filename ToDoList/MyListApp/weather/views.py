from django.shortcuts import render
from .utils import get_weather_data
from django.conf import settings

   
def weather_view(request):
    weather_data = {}
    if 'city_or_zip' in request.GET:
        city_or_zip = request.GET.get('city_or_zip')
        api_key = settings.OPENWEATHERMAP_API_KEY
        weather_data = get_weather_data(city_or_zip, api_key)
    
    return render(request, 'weather/weather_check.html', {
        'weather_data': weather_data,
        })
