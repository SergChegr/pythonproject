import sqlite3
import datetime
import requests



connection = sqlite3.connect("D:\\itstep_DB.sl3")

c = connection.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS weather
            (date_time TEXT, temperature REAL)''')


connection.commit()

connection.close()



url = 'https://ua.sinoptik.ua/погода-маріуполь'

response = requests.get(url)


if response.status_code == 200:

   html = response.content

else:

   print('Не вдалося отримати сторінку')

from bs4 import BeautifulSoup


soup = BeautifulSoup(html, 'html.parser')

today_weather = soup.find('div', {'class': 'weatherToday'}).find('div', {'class': 'temperature'}).text
today_temperature = int(today_weather.split('°')[0])


print(f"Температура сьогодні: {today_temperature}°C")


temperature = today_temperature

date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


conn = sqlite3.connect('weather.db')

c = conn.cursor()


c.execute("INSERT INTO weather VALUES (?, ?)", (date_time, temperature))


conn.commit()

conn.close()