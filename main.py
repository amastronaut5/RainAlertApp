import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key="5d0fab0d04689861d83c0c8bbcff45a4"
account_sid = 'AC9e7c7285102b06d382e469700e892b1e'
auth_token = "3115345677344ede9e53f58f82131ce0"
LATITUDE = 31.820210
LONGITUDE = 75.198730
weather_params = {
    "lat":LATITUDE,
    "lon":LONGITUDE,
    "appid":api_key,
    "cnt":4

}

response = requests.get(OWN_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="IT'S GOING TO RAIN TODAY. REMEMBER TO BRING AN ☔",
        from_='+16562233500',
        to='+919877918214'
    )
    print(message.status)