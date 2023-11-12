import requests


class WeatherAPIClient:
    def __init__(self):
        self.base_url = "https://api.weatherapi.com/v1"
        self.api_key = "6da923aa568b47c49fd151817232809"

    def get_current_temperature(self, city):
        response = requests.get(
            f'{self.base_url}/current.json?key={self.api_key}&q={city}')
        data = response.json()
        if "current" in data:
            return data["current"]["temp_c"]
        else:
            return None

    def get_temperature_after(self, city, days, hour=None):
        response = requests.get(
            f'{self.base_url}/forecast.json?key={self.api_key}&q={city}&days={days}&hour={hour}')
        data = response.json()

        if hour is not None and "forecast" in data:
            return data["forecast"]["forecastday"][0]["hour"][0]["temp_c"]
        elif "forecast" in data:
            return data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]

        else:
            return None

    def get_lat_and_long(self, city):
        response = requests.get(
            f'{self.base_url}/search.json?key={self.api_key}&q={city}')
        data = response.json()
        if data:
            return data[0]["lat"], data[0]["lon"]
        else:
            return None


# weather = WeatherAPIClient()

# print(weather.get_current_temperature("cairo"))
# print(weather.get_temperature_after("cairo", 3, 6))
# print(weather.get_lat_and_long("cairo"))

while True:
    weather = WeatherAPIClient()

    print('\033[93m' + "Weather Information Retrieval App"+'\033[0m')
    print("1. Get current temperature")
    print("2. Get temperature after specific days and hour")
    print("3. Get latitude and longitude")
    print("4. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        city = input("Enter the city: ")
        current_temp = weather.get_current_temperature(city)
        if current_temp is not None:
            print(
                '\033[92m' + f"Current temperature in {city}: {current_temp}°C"+'\033[0m')
        else:
            print(
                '\033[91m' + f"Could not retrieve current temperature for {city}."+'\033[0m')
    elif choice == "2":
        city = input("Enter the city: ")
        while True:
            days = input("Enter the number of days: ")
            hour = input(
                "Enter the hour (optional, enter 0 if not specified): ")
            if days.isdigit() and hour.isdigit():
                days = int(days)
                hour = int(hour)
                break
            else:
                print('\033[91m' +
                      f"days and hour must be numbers"+'\033[0m')
        future_temp = weather.get_temperature_after(city, days, hour)
        if future_temp is not None:
            print(
                '\033[92m' + f"Temperature in {city} after {days} days and {hour} hours: {future_temp}°C"+'\033[0m')
        else:
            print('\033[91m' +
                  f"Could not retrieve future temperature for {city}."+'\033[0m')
    elif choice == "3":
        city = input("Enter the city: ")
        lat, lon = weather.get_lat_and_long(city)
        if lat is not None and lon is not None:
            print(
                '\033[92m' + f"Latitude and longitude of {city}: Latitude {lat}, Longitude {lon}"+'\033[0m')
        else:
            print(
                '\033[91m' + f"Could not retrieve latitude and longitude for {city}."+'\033[0m')
    elif choice == '4':
        print('\033[93m' + "Goodbye!" + '\033[0m')
        break
    else:
        print(
            '\033[91m' + "Invalid choice. Please select a valid option." + '\033[0m')
