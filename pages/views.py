from django.shortcuts import render, get_object_or_404, Http404
from . models import News, Project
import os
import requests
import pyowm
API_KEY=os.environ.get('OWM_API')
owm = pyowm.OWM(API_KEY)
# fc = owm.three_hours_forecast('Banjul,GMB')
# current_weather = owm.weather_at_place('Banjul,GMB')
def home(request):
    try:
        #handle search field
        if 'city' in request.GET:
            city = request.GET['city']
            fc = owm.three_hours_forecast(city)
            current_weather = owm.weather_at_place(city)
        # getting current weather forecast
            w = current_weather.get_weather()
            loc = current_weather.get_location()
            c_weather = []
            weather_now ={
                'temp':round(w.get_temperature('celsius')['temp']),
                'wind_speed': w.get_wind()['speed'],
                'wind_deg':w.get_wind(),
                'status': w.get_detailed_status(),
                'humidity':w.get_humidity(),
                'icon':w.get_weather_icon_url(),
                'time':w.get_reference_time(timeformat='date')
            }
            c_weather.append(weather_now)
            # getting a three_hourly weather forecast 
            f = list(fc.get_forecast())[:6]
            weather_data = []
            for weather in f:
                weather_con = {
                    'temp' : round(weather.get_temperature(unit='celsius')['temp']),
                    'temp_max' :round(weather.get_temperature(unit='celsius')['temp_max']),
                    'temp_min' : round(weather.get_temperature(unit='celsius')['temp_min']),
                    'icon':weather.get_weather_icon_url(),
                    'time':weather.get_reference_time(timeformat='date')
                }
                weather_data.append(weather_con)
            context = {
                'c_weather':c_weather[0],
                'weather': weather_data,
                'city':loc.get_name()
            }
            return render(request, 'pages/home.html', context)
        else:
            city = 'Banjul'
            fc = owm.three_hours_forecast(city)
            current_weather = owm.weather_at_place(city)

            # getting current weather forecast
            w = current_weather.get_weather()
            c_weather = []
            weather_now ={
                'temp':round(w.get_temperature('celsius')['temp']),
                'wind_speed': w.get_wind()['speed'],
                'wind_deg':w.get_wind(),
                'status': w.get_detailed_status(),
                'humidity':w.get_humidity(),
                'icon':w.get_weather_icon_url(),
                'time':w.get_reference_time(timeformat='date')
            }
            c_weather.append(weather_now)
            # getting a three_hourly weather forecast 
            f = list(fc.get_forecast())[:6]
            weather_data = []
            for weather in f:
                weather_con = {
                    'temp' : round(weather.get_temperature(unit='celsius')['temp']),
                    'temp_max' : round(weather.get_temperature(unit='celsius')['temp_max']),
                    'temp_min' : round(weather.get_temperature(unit='celsius')['temp_min']),
                    'icon':weather.get_weather_icon_url(),
                    'time':weather.get_reference_time(timeformat='date')
                }
                weather_data.append(weather_con)
            context = {
                'c_weather':c_weather[0],
                'weather': weather_data,
                'city':city
            }
            return render(request, 'pages/home.html', context)
    except:
        raise Http404


def news(request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request, 'pages/news.html', context)
def detail_news(request, id):
    news = get_object_or_404(News, id=id)
    context = {
        'news':news
    }
    return render(request, 'pages/news_detail.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'pages/projects.html', context)

def detail_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        'project':project
    }
    return render(request, 'pages/detail_project.html', context)


def contacts(request):
    return render(request, 'pages/contact.html')
