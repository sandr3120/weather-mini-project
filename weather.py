import requests
import os
from dotenv import load_dotenv

load_dotenv()
api = os.getenv('API_key')

class City:
    def __init__(self,name,lat,lon,units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()
    
    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={api}")   

        except(requests.exceptions.ConnectionError): 
            print("You're offline. Check your connection.")

        data = (response.json())
        self.temp = data["main"]["temp"]
        self.feels_like = data["main"]["feels_like"]
        self.main = data["weather"][0]["main"]
        self.description = data["weather"][0]["description"]
        self.humidity = data["main"]["humidity"]
        self.visibility = data["visibility"]
        self.country = data["sys"]["country"]
    
    def display_data(self):
        unit = "C"
        if self.units == "imperial":
            unit = "F"

        print(f"{self.name}, {self.country}\n{self.temp}°{unit}\nFeels like {self.feels_like}°{unit}. {self.main}. {self.description}\nHumidity: {self.humidity}\tVisibility: {self.visibility}")
        print()




city1 = City("Tokyo",35.652832,139.839478,"imperial")
city1.display_data()
city2 = City("India",22,77)
city2.display_data()