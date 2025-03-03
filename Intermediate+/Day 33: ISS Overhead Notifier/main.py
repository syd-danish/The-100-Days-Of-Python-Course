import requests
from datetime import datetime
import smtplib
import time

MY_GMAIL="yasindanish13@gmail.com"
MY_PASSWORD="mypassword" #enter your appropriate "app password"
MY_LAT=25.346254
MY_LONG=55.420933


def iss():
    response_iss = requests.get('http://api.open-notify.org/iss-now.json')
    iss_position = response_iss.json()['iss_position']
    iss_longitude = float(iss_position['longitude'])
    iss_latitude = float(iss_position['latitude'])
    #iss_position = (iss_longitude, iss_latitude)
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True

def night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data = response_sun.json()
    sunrise = data['results']['sunrise'].split('T')
    sunset = data['results']['sunset'].split('T')
    time_now = datetime.now().hour
    sunrise_hour = int(sunrise[1].split(':')[0])
    sunset_hour = int(sunset[1].split(':')[0])

    if time_now>= sunset or time_now<=sunrise:
        return True
if iss() and night():
    time.sleep(60)
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_GMAIL,password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_GMAIL, to_addrs=MY_GMAIL,msg="Subject: LOOK UP!\n\n The ISS might be right above you in the sky!")
