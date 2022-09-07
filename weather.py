#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

from xftts import xftts

request = requests.get('http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%A4%A9%E6%B0%94&rsv_pq=aa29735400047032&rsv_t=2de3M%2Fa3Q6d9M4ZgEeskti6n6VkjchWXDfNZaIXrbLgh0MwmMTkEU5pKg78&rsv_enter=1&rsv_sug3=9&rsv_sug1=12&rsv_sug2=0&inputT=2695&rsv_sug4=3191&rsv_sug=2')

soup = BeautifulSoup(request.text)

date =  soup.find_all("p", class_="op_weather4_twoicon_date")[0].get_text().strip().replace(' ',',').replace('实时','实时温度')
temp =  soup.find_all("p", class_="op_weather4_twoicon_temp")[0].get_text().strip()
weath =  soup.find_all("p", class_="op_weather4_twoicon_weath")[0].get_text().strip()
wind =  soup.find_all("p", class_="op_weather4_twoicon_wind")[0].get_text().strip()
pm25 =  soup.find_all("p", class_="op_weather4_twoicon_pm25")[0].get_text().strip().replace(' ','').replace('实时空气质量:','PM2.5数量,').replace('\n','').replace('\xa0',',空气质量,') 

msg = 'sound111,今天是'+date+',天气,'+weath+","+wind+","+temp +","+pm25

tts = xftts('/dev/ttyUSB0')

print(msg)
tts.say(msg)

