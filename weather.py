import json
import requests
from location import *

def parse_request():
    api_key = ""
    units = "metric"
    location = get_location()
    city = location[0]
    country = location[1]
    Weatherinfo = {"Location": "Unknown", "Description": "Unknown", "Icon": "Unknown", "Background": "Unknown","Temperature": "Unknown", "Humidity": "Unknown",
                    "Wind_speed": "Unknown", "Pressure": "Unknown", "Feels_like": "Unknown", "Visibility": "Unknown", "Wind_direction": "Unknown" }
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    weather_main_url = "http://api.openweathermap.org/data/2.5/weather?q="+city+","+country+"&units="+units+"&appid="+api_key 

    response = requests.get(weather_main_url)
    json_response = response.json()
    
    if json_response["cod"] == 400:
        print("\n Nothing to geocode \n")

    elif json_response["cod"] == 401:
        print("\n Invalid API key. Please see http://openweathermap.org/faq#error401 for more info. \n")
        
    elif json_response["cod"] == 404:
        print("\n City not found. Please see http://openweathermap.org/faq#error404 for more info. \n")
        
    elif json_response["cod"] == 429:
        print("\n You have free tariff and make more than 60 API calls per minute. Please see http://openweathermap.org/faq#error429 for more info. \n")
        
    elif 'weather' not in json_response or 'main' not in json_response or 'wind' not in json_response:
        print(json_response)
        print("\n \"weather\" or \"main\" or \"wind\" not in response \n")
        
    else:
        Weatherinfo["Location"] = city
        Weatherinfo["Description"] = json_response["weather"][0]["description"]
        Visual_description = json_response["weather"][0]["icon"]
        Weatherinfo["Icon"] = "static/images/" + Visual_description + ".png"
        Weatherinfo["Background"] = "/static/images/" + Visual_description + "_art.jpg"
        Weatherinfo["Temperature"] = str(round(json_response["main"]["temp"])) + "˚C"
        Weatherinfo["Humidity"] = str(json_response["main"]["humidity"]) + "%"
        Weatherinfo["Wind_speed"] = str(round(json_response["wind"]["speed"])) + " m/s"
        Weatherinfo["Pressure"] = str(json_response["main"]["pressure"]) + " mb"
        Weatherinfo["Feels_like"] = str(json_response["main"]["feels_like"]) + "˚C"
        Visibility_km = int(json_response["visibility"]) / 1000
        Weatherinfo["Visibility"] = str(Visibility_km) + " km"
        ix = round(json_response["wind"]["deg"] / (360. / len(dirs)))
        Weatherinfo["Wind_direction"] = dirs[ix % len(dirs)]

    return Weatherinfo