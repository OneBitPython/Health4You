import requests
import folium
import webbrowser
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import os

load_dotenv()


class FindNearbyHospitals:
    def __init__(self):
        self.url_for_nearby_hospitals = os.getenv("url_for_nearby_hospitals")
        self.api_key_for_nearby_hospitals = os.getenv(
            "api_key_for_nearby_hospitals")
        self.api_key_for_getting_lat_long = os.getenv(
            "api_key_for_getting_lat_long")

    def get_latitude_longitude(self, place):
        geolocator = Nominatim(user_agent=self.api_key_for_getting_lat_long)
        location = geolocator.geocode(place)
        return location.latitude, location.longitude

    def find_nearby_hospitals(self, place):
        error = False
        try:
            latitude, longitude = self.get_latitude_longitude(place)
        except:
            error = True

        if error == False:
            PARAMS = {
                'apikey': self.api_key_for_nearby_hospitals,
                'q': "hospitals",
                'limit': 5,
                'at': '{},{}'.format(latitude, longitude)
            }

            r = requests.get(url=self.url_for_nearby_hospitals, params=PARAMS)
            data = r.json()

            main_coords = [latitude, longitude]
            place_coords = []
            place_details = []

            all_hospitals = []
            for i in data['items']:
                val = []
                hospital_details = ""
                try:
                    val.append(i['title']+'\n')
                    hospital_details += "Name: " + i['title'] + '\n'
                except:
                    pass
                try:
                    hospital_details += "Address: " + \
                        i['address']['label'] + '\n'
                except:
                    pass
                try:
                    place_coords.append(
                        [i['position']['lat'], i['position']['lng']])
                    hospital_details += "Lat: " + \
                        str(i['position']['lat']) + " Long: " + \
                        str(i['position']['lng']) + '\n'
                except:
                    pass
                try:
                    val.append(i['contacts'][0]['phone'][0]['value']+'\n')
                    hospital_details += "Phone num: " + \
                        i['contacts'][0]['phone'][0]['value'] + '\n'

                except:
                    pass
                place_details.append(val)
                all_hospitals.append(hospital_details)
            self.draw_map(main_coords, place_coords, place_details)
            return all_hospitals

    def draw_map(self, main_coords, place_coords, place_details):
        maps = folium.Map(location=main_coords,
                          zoom_start=12, tiles='Stamen Terrain')
        for i, j in zip(place_coords, place_details):

            folium.Marker(i,
                          popup=j).add_to(maps)
        maps.save("maps/maps.html")
