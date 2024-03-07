import json
import sys
import requests
from datetime import datetime

# computer location from command line arguments
if len(sys.argv) < 2:
    print("Usage: quickweather.py location")
    sys.exit()

location = ' '.join(sys.argv[1:])

# Download the json data from openweathermap.org API
url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=55afe9bd160735d2643dacfd706b1057" % location
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

data = weatherData['weather']
print('Current weather in %s:' % location)
print(data[0]['main'], "-", data[0]['description'])

temp = weatherData['main']
print('Temperature is:', temp['temp'] - 273.15, "C")

# Retrieve sunrise and sunset times if available
if 'sys' in weatherData:
    sys_data = weatherData['sys']
    if 'sunrise' in sys_data and 'sunset' in sys_data:
        sunrise_timestamp = sys_data['sunrise']
        sunset_timestamp = sys_data['sunset']
        sunrise_time = datetime.fromtimestamp(sunrise_timestamp)
        sunset_time = datetime.fromtimestamp(sunset_timestamp)
        print("Sunrise time:", sunrise_time.strftime('%Y-%m-%d %H:%M:%S'))
        print("Sunset time:", sunset_time.strftime('%Y-%m-%d %H:%M:%S'))
