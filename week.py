import requests
import json
from pprint import pprint
import tkinter as tk
from datetime import datetime

key = "6e8428be179aba1530895e84b5b3cf40"

params = {
    "lat": 34.6913,
    "lon": 135.183,
    "exclude": "current,minutely,alerts",
    "appid": key,
    "units": "metric",
    "lang": "ja"
}
three_hour_url = f"https://api.openweathermap.org/data/2.5/forecast"
seventh_url = f"https://api.openweathermap.org/data/2.5/onecall"

jsondata = requests.get(three_hour_url,params=params).json()
# pprint(jsondata)

# for item in jsondata["list"]:
#     print(item["dt_txt"])

for item in jsondata["list"][:8]:
    print("日時　　 =",item["dt_txt"])
    print("気温　　 =",item["main"]["temp"])
    print("天気　　 =",item["weather"][0]["description"])
    print("アイコン",item["weather"][0]["icon"])
    print("風速　　 =",item["wind"]["speed"])
    print("降水確率 =",item["pop"])
    print("")

""" # 今日の日付（YYYY-MM-DD）
today = datetime.now().strftime("%Y-%m-%d")

for item in jsondata["list"]:
    dt_txt = item["dt_txt"]  # "2026-04-06 03:00:00"

    date_part, time_part = dt_txt.split(" ")

    # 条件：今日 + 03:00〜24:00
    if date_part == today and "00:00:00" <= time_part <= "23:59:59":
        print("日時　　 =",dt_txt)
        print("気温　　 =",item["main"]["temp"])
        print("天気　　 =",item["weather"][0]["description"])
        print("風速　　 =",item["wind"]["speed"])
        print("降水確率 =",item["pop"])
        print("") """

""" # 今日の日付（YYYY-MM-DD）
today = datetime.now().strftime("%Y-%m-%d")

for item in jsondata["list"]:
    dt = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")

    # 条件：今日 + 03:00〜24:00
    if dt.date() == datetime.now().date() and  0 <= dt.hour <= 23:
        print("日時 =", item["dt_txt"])
        print("気温 =", item["main"]["temp"])
        print("天気　　 =",item["weather"][0]["description"])
        print("風速　　 =",item["wind"]["speed"])
        print("降水確率 =",item["pop"])
        print("") """

""" print("都市名　 =",jsondata["city"]["name"])
print("日時　　 =",jsondata["list"][0]["dt_txt"])
print("気温　　 =",jsondata["list"][0]["main"]["temp"])
print("天気　　 =",jsondata["list"][0]["weather"][0]["description"])
print("風速　　 =",jsondata["list"][0]["wind"]["speed"])
print("降水確率 =",jsondata["list"][0]["pop"]) """

""" city = "Kobe,jp"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"

jsondata = requests.get(url).json()
pprint(jsondata)
print("都市名　 =",jsondata["name"])
print("気温　　 =",jsondata["main"]["temp"])
print("天気　　 =",jsondata["weather"][0]["main"])
print("天気詳細 =",jsondata["weather"][0]["description"]) """