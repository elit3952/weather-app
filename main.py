import requests
from constants.settings import API_URL
from datetime import datetime
from utils.save_to_excel import save_to_excel
from utils.save_to_sql import save_to_sql
import time


def save_file(formated_data):
    pass


def weather_data():
    try:
        response=requests.get(API_URL)
        data=response.json()
        formated_data={
            "Temperatura":data['main']['temp'],
            "Odczuwalna temp":data['main']['feels_like'],
            "Zachmurzenie":data['clouds']['all'],
            "Cisnienie":data['main']['pressure'],
            "Wilgotnosc":data['main']['humidity'],
            "Wiatr":data['wind']['speed'],
            "Opis":data['weather'][0]['description'],
            "Data":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_to_excel(formated_data)
        save_to_sql(formated_data)

    except Exception as err:
        print("Wystapil blad", err)
        
while True:
    weather_data()
    time.sleep(10)