import json
import geocoder

def get_location(city_name, users_ip):

    if city_name:
        g = geocoder.osm(city_name)
        response = g.json
        
        splited_city_name = city_name.split(',')
        city = splited_city_name[0]
        lat = str(response['lat'])
        lon = str(response["lng"])

        return(city, lat, lon)

    else:
        ip = str(users_ip)

        g = geocoder.ipinfo(ip)
        response = g.json

        city = str(response['city'])
        lat = str(response['lat'])
        lon = str(response["lng"])

        return(city, lat, lon)
