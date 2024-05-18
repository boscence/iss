from geopy.geocoders import Nominatim

def get_location_data(latitude, longitude):
    print(latitude, longitude)
    geolocator = Nominatim(user_agent="iss_info")
    location = geolocator.reverse([latitude, longitude],  language="en")
    if location == None:
         return "Ocean"
    else:
        return dict([location])


#get_location_data(30.949641, 121.805064)