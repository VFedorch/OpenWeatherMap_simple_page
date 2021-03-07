import json
import time
import requests
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    weather = parse_request()
    return render_template('index.html', item=weather)

def get_location():
    get_location_url = 'http://ipinfo.io/json'

    response = requests.get(get_location_url)
    location_response = response.json()

    city = location_response['city']
    country = location_response['country']

    return(city, country)

def parse_request():
    api_key = ""
    units = "metric"
    location = get_location()
    city = location[0]
    country = location[1]
    weather_main_url = "http://api.openweathermap.org/data/2.5/weather?q="+city+","+country+"&units="+units+"&appid="+api_key 

    response = requests.get(weather_main_url)
    json_response = response.json()
    
    Weatherinfo = dict()
    Weatherinfo['Location'] = "Showing Weather for: " + city
    Weatherinfo['Description'] = "Current atmospheric description: " + json_response["weather"][0]["description"]
    Visual_description = json_response["weather"][0]["icon"]
    Weatherinfo['Icon'] = "static/images/" + Visual_description + "_icon.png"
    Weatherinfo['Background'] = "static/images/" + Visual_description + "_art.jpg"
    Weatherinfo['Temperature'] = "Current Temperature:" + str(round(json_response["main"]["temp"])) + "˚C"
    Weatherinfo['Humidity'] = "Humidity:" + str(json_response["main"]["humidity"]) + "%"
    Weatherinfo['Wind_speed'] = "Wind speed:" + str(round(json_response["wind"]["speed"])) + "mph"
    Weatherinfo['Pressure'] = "Atmospheric Pressure:" + str(json_response["main"]["pressure"]) + "mmRs"

    return Weatherinfo

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)