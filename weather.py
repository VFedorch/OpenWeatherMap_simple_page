import json
import time
import requests
from location import *

def weather(form_or_button):

    api_key = ""
    units = "metric"
    city_name = form_or_button
    location = get_location(city_name)
    city = location[0]
    lat = location[1]
    lon = location[2]
    response_forecast = []
    seven_days_forecast = []
    current_weather = {"Location": "Unknown", "Description": "Unknown", "Icon": "Unknown", "Background": "Unknown","Temperature": "Unknown", "Humidity": "Unknown",
                    "Wind_speed": "Unknown", "Pressure": "Unknown", "Feels_like": "Unknown", "Visibility": "Unknown", "Wind_direction": "Unknown" }
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    main_url = "http://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon=" + lon + "&units=" + units + "&exclude=hourly,minutely,alerts&appid=" + api_key

    response = requests.get(main_url)
    json_response = response.json()

    if "cod" in json_response:
        print(str(json_response["cod"]) + ": " + json_response["message"])
    else:
        response_current = json_response["current"]
        response_forecast = json_response["daily"]

        current_weather["Location"] = city
        current_weather["Description"] = response_current["weather"][0]["description"]
        Visual_description = response_current["weather"][0]["icon"]
        current_weather["Icon"] = "static/images/icons/" + Visual_description + ".png"
        current_weather["Background"] = "/static/images/arts/" + Visual_description + "_art.jpg"
        current_weather["Temperature"] = str(round(response_current["temp"])) + "˚C"
        current_weather["Humidity"] = str(response_current["humidity"]) + "%"
        current_weather["Wind_speed"] = str(round(response_current["wind_speed"])) + " m/s"
        current_weather["Pressure"] = str(response_current["pressure"]) + " mb"
        current_weather["Feels_like"] = str(response_current["feels_like"]) + "˚C"
        Visibility_km = int(response_current["visibility"]) / 1000
        current_weather["Visibility"] = str(Visibility_km) + " km"
        ix = round(response_current["wind_deg"] / (360. / len(dirs)))
        current_weather["Wind_direction"] = dirs[ix % len(dirs)]

        for item in response_forecast:

            forecast = {}

            epoch = item["dt"]
            date = time.strftime("%a, %d %b", time.localtime(epoch))
            today = time.strftime("%a, %d %b", time.localtime(time.time()))
            
            if date == today:
                forecast["Date"] = "Today"
            else:
                forecast["Date"] = date

            Visual_description = item["weather"][0]["icon"]
            forecast["Icon"] = "static/images/icons/" + Visual_description + ".png"
            forecast["Description"] = item["weather"][0]["description"]
            forecast["Temperature"] = str(round(item["temp"]["min"])) + ".." + str(round(item["temp"]["max"])) + "˚C"
            forecast["Humidity"] = str(item["humidity"]) + "%"
            forecast["Pressure"] = str(item["pressure"]) + " mb"
            forecast["Wind_speed"] = str(round(item["wind_speed"])) + " m/s"
            
            seven_days_forecast.append(forecast)
    
    return current_weather, seven_days_forecast
