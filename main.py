from location import *

api_key = ""
units = "metric"
location = get_location()
city = location[0]
country = location[1]
Weatherinfo = {"Location": "Unknown", "Description": "Unknown", "Icon": "Unknown", "Background": "Unknown","Temperature": "Unknown", "Humidity": "Unknown",
                "Wind_speed": "Unknown", "Pressure": "Unknown", "Feels_like": "Unknown", "Visibility": "Unknown", "Wind_direction": "Unknown" }
dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
weather_main_url = "http://api.openweathermap.org/data/2.5/weather?q="+city+","+country+"&units="+units+"&appid="+api_key 
forecast_main_url = "http://api.openweathermap.org/data/2.5/forecast?q="+city+","+country+"&units="+units+"&appid="+api_key 

def cods(json_response):
    if json_response["cod"] == 400:
        print("\n Nothing to geocode \n")

    elif json_response["cod"] == 401:
        print("\n Invalid API key. Please see http://openweathermap.org/faq#error401 for more info. \n")
        
    elif json_response["cod"] == 404:
        print("\n City not found. Please see http://openweathermap.org/faq#error404 for more info. \n")
        
    elif json_response["cod"] == 429:
        print("\n You have free tariff and make more than 60 API calls per minute. Please see http://openweathermap.org/faq#error429 for more info. \n")
        
    elif 'list' not in json_response:
        print(json_response)
        print("\n \"list\"  not in response \n")