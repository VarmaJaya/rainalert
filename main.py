


import requests
from twilio.rest import Client
# step1 : Calling the Weather API and storing your location data 
import json
LATITUDE = "Your location latitude (Replace your data here)"
LANGITUDE = "Your location langitude (Replace your data here)"
API_KEY = "API key from weather API (Replace your data here)"
CNT = 3
account_sid = 'Account ID from twilio(Replace your data here)'
auth_token = 'api token from twilo (Replace your data here)'

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat":LATITUDE,
    "lon":LANGITUDE,
    "cnt":CNT,
    "appid":API_KEY
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()



# step2: checking weathert based on the data we got from weather api
will_rain = False

for hour_data in data["list"]:
   condition = hour_data["weather"][0]["id"]
   if condition < 700:
      will_rain = True

# step3: if there is a chance of rain then sending an message to your mobile number
if will_rain:
   client = Client(account_sid, auth_token)
   message = client.messages.create(
   body="It's going to rain today, remember to bring an umbrella ☔",
   from_='Twilio temparary number (Replace your data here)',
   to='your number'
   )
   print(message.status)