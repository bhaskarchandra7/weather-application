from django.shortcuts import render , redirect
from django.http import HttpResponse
import json
import urllib.request


# Create your views here.
def index(request):
    if request.method=="POST":
        city=request.POST["city"]
        api_key = 'a374d19ce286044721e718c9f56803d1' 
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        res = urllib.request.urlopen(url).read().decode('utf-8')
        json_data=json.loads(res)
        country_code = json_data.get('sys', {}).get('country', None)
        temp = json_data.get('main', {}).get('temp', None)
        pressure = json_data.get('main', {}).get('pressure', None)
        
        data = {
            "country_code": country_code,
            "temp": str(temp) + 'k' if temp else None,
            "pre": str(pressure) if pressure else None,
        }
    else:
        data = {}
    return render(request, 'index.html',data)

def signup(request):
    return render(request, template_name="signup.html")
def login(request):
    return render(request, template_name="login.html")
