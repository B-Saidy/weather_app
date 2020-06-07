from django.shortcuts import render, get_object_or_404, Http404,redirect
from . models import News, Project, Service,Contact, Media
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
            f = list(fc.get_forecast())[:8]
            weather_data = []
            services = Service.objects.all()
            media = Media.objects.all()
            media_items = []
            for m in media:
                media_items.append(m)
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
                'city':loc.get_name(),
                'services' : services,
                'caro1': media_items[0],
                'caro2': media_items[1],
                'caro3': media_items[2],
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
            f = list(fc.get_forecast())[:8]
            weather_data = []
            services = Service.objects.all()
            media = Media.objects.all()
            media_items = []
            for m in media:
                media_items.append(m)
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
                'city':city,
                'services': services,
                'caro1': media_items[0],
                'caro2': media_items[1],
                'caro3': media_items[2],
            }
            return render(request, 'pages/home.html', context)
    except:
        return redirect('api_timeout')


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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        company = request.POST['company']
        text = request.POST['text']
        
        contact = Contact(name=name, email=email, company_name=company, text=text)
        contact.save()
        return redirect('contacts')
    return render(request, 'pages/contact.html')

def service(request, id):
    service = get_object_or_404(Service, id=id)
    context = {
        'service': service
    }
    return render(request, 'pages/service.html', context)

def api_timeout(request):
    services = Service.objects.all()
    media = Media.objects.all()
    media_items = []
    for m in media:
        media_items.append(m)
    context = {
        'services': services,
        'caro1': media_items[0],
        'caro2': media_items[1],
        'caro3': media_items[2],
    }
    return render(request, 'pages/api_call_timeout.html', context)


