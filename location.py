import json
import requests
import geocoder

def get_location(city_name):
    get_location_url = 'http://ipinfo.io/json'

    if city_name:
        g = geocoder.osm(city_name)
        response = g.json

        print("\n" + str(response))
        
        splited_city_name = city_name.split(',')
        city = splited_city_name[0]
        lat = str(response['lat'])
        lon = str(response["lng"])

        return(city, lat, lon)

    else:
        response = requests.get(get_location_url)
        location_response = response.json()

        city = location_response['city']
        location = location_response['loc']
        lat, lon = location.split(',')

        return(city, lat, lon)
