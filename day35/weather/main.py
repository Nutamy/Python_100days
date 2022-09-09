import requests
from twilio.rest import Client

account_sid = 'AC40033c9f14d7c0e6a93e0902f701276f'
auth_token = '0aa27fecc9cbdde4077e8f13c25ee40c'
client = Client(account_sid, auth_token)


# =-==-==-==-==-==-==-==-=WEATHER=-==-==-==-==-==-==-==-==-==-==-==-==-=
api_key = "8b682e300f8818e7cc6238b05b3fc814"
city_name = "Almaty"
my_params = {
    "q": city_name,
    "appid": api_key
}
api = f"https://api.openweathermap.org/data/2.5/weather"
response = requests.get(api, params=my_params).json()
print(response)
temperature_Kelvin = response["main"]["temp"]
temperature_C = round(temperature_Kelvin - 273.15, 1)
print(temperature_C)
weather = response["weather"][0]["id"]
weather_predict = ''
if 599 > weather > 499:
    weather_predict = "You should take an umbrella. Today is rain! ☔"
elif 699 > weather > 599:
    weather_predict = "You should wear warm clothes and gloves. Today is snow! ☃"
elif 299 > weather > 199:
    weather_predict = "Wow, stay at home! Today is a thunderstorm.⛈️"
elif weather == 800:
    weather_predict ="Have a lovely sunny day! ☀️"
elif 399 > weather > 299:
    weather_predict = "A cup of hot coffee could help you. Today is a drizzle.🌧️"
elif weather > 800:
    weather_predict = "Look up at the sky! There are some clouds! Have a nice day!⛅"
elif 699 > weather > 799:
    weather_predict ="Can you see something? It looks like a fog, mist, smoke, dust, or haze.😶‍🌫️"


# =-==-==-==-==-==-==-==-=SMS=-==-==-==-==-==-==-==-==-==-==-==-==-=
message = client.messages.create(
    messaging_service_sid='MG61beb39bf43f351d6501de843a419445',
    body=f'Good morning, {city_name}!\n '
         f'{weather_predict}\n'
         f'T={temperature_C}°C',
    to='+77059536514'
)

print(message.status)