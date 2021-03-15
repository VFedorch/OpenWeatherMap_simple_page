import json
import requests
from main import *

def weather():
    response = requests.get(weather_main_url)
    json_response = response.json()
    
    if json_response["cod"] != 200:
        cods(json_response)
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
