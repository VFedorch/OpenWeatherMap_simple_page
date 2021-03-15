import json
import requests

def get_location():
    get_location_url = 'http://ipinfo.io/json'

    response = requests.get(get_location_url)
    location_response = response.json()

    city = location_response['city']
    country = location_response['country']

    return(city, country)
    