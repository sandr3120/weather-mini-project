import requests

try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=35.652832&lon=139.839478&appid={key}")   

except(requests.exceptions.ConnectionError): 
    print("You're offline. Check your connection.")

data = (response.json())
temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
main = data["weather"][0]["main"]
description = data["weather"][0]["description"]
humidity = data["main"]["humidity"]
visibility = data["visibility"]
country = data["sys"]["country"]

print(f"Tokyo Perfecture, {country}\n{temp}°C\nFeels like {feels_like}°C. {main}. {description}\nHumidity: {humidity}\tVisibility: {visibility}")

class City:
    def __init__(self,name,lat,lon,units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units

city1 = City("Tokyo Perfecture",35.652832,139.839478)