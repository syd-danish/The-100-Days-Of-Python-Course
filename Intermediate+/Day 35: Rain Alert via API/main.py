import requests
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient



API_KEY='478e6b407b0813954046a9cfa4523587'
OPEN_WEATHER_MAP_ENDPOINT='https://api.openweathermap.org/data/2.5/forecast'

TWILIO_ACCOUNT_SID='<ENTER YOUR UNIQUE TWILIO ACCOUNT SID>'
TWILIO_AUTH_TOKEN='<ENTER YOUR UNIUE TWILIO AUTHORIZATION TOKEN>'

PARAMS={
    'lat':25.346254,
    'lon':55.420933,
    'appid': API_KEY,
    'cnt':4,
}

proxy_client= TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}
response=requests.get(OPEN_WEATHER_MAP_ENDPOINT,params=PARAMS)
json_file=response.json()


weather_id=json_file['list'][0]['weather'][0]['id']
print(weather_id)
j=0
while j<len(json_file)-1:
    weather_id=json_file['list'][j]['weather'][0]['id']
    if weather_id<700:
        client=Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,http_client=proxy_client)
        message=client.messages.create(
            from_="whatsapp: <ENTER YOUR TWILIO NUMBER>",
            body=" RAIN ALERT!\n It's going to rain today! Please take your umbrella if you plan to outside!",
            to="whatsapp: <ENTER YOUR WHATSAPP NUMBER>"
        )
        print('bring an umbrella')
        break
    j+=1
