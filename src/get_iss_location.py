import requests


def get_iss_location():
    location = requests.get('http://api.open-notify.org/iss-now.json')
    location_json = location.json()

    return location_json['iss_position']
