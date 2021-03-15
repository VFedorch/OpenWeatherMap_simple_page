import json
import requests
from main import *

def forecast():
    response = requests.get(forecast_main_url)
    json_response = response.json()
    
    if json_response["cod"] != 200:
        cods(json_response)
    else:
        forecast_info = {}
        for item in json_response["list"]:
            direct_datetime = item['dt_txt']

            weather_info = {}

            weather_info["Description"] = item["weather"][0]["description"]
            visual_description = item["weather"][0]["icon"]
            weather_info["Icon"] = "static/images/" + visual_description + ".png"
            weather_info["Temperature"] = str(round(item["main"]["temp"])) + "˚C"
            weather_info["Humidity"] = str(item["main"]["humidity"]) + "%"
            weather_info["Pressure"] = str(item["main"]["pressure"]) + " mb"
            
            direct_date, direct_time = direct_datetime.split(' ')
            year, month, day = direct_date.split('-')
            date = month + "." + day
            time = direct_time[:5]

            forecast_info.update({date+" "+time:weather_info})

        print(forecast_info)

forecast()
