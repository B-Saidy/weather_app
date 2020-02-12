import os
import requests
API_KEY=os.environ.get('OWM_API')
city = 'Banjul'
from django.shortcuts import render
# url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
weather = {'temp': 21, 'feels_like': 20.4, 'temp_min': 21, 'temp_max': 21, 'pressure': 1011, 'humidity': 68}
def home(request):
    # r = requests.get(url.format(city, API_KEY)).json()
    # weather = r['main']
    context = {
        'weather':weather
    }
    return render(request, 'pages/home.html', context)
