import json
import requests
import geocoder
from OWM_page import *

def get_location(city_name, users_ip):

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
        ip = str(users_ip)
        print("\n", users_ip)

        g = geocoder.ipinfo(ip)
        response = g.json
        print("\n" + str(response))

        city = str(response['city'])
        lat = str(response['lat'])
        lon = str(response["lng"])

        return(city, lat, lon)
