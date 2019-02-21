#! python
#  get weather data from all my weather sites with apis

import requests
import bs4
import json
from apixu.client import ApixuClient, ApixuException
from credentials import *
import urllib.request as req



def getApixu(ApiKey):
    # create the Apixu client obj & query current & 7 forecast weather data

    try:
        client = ApixuClient(ApiKey)
        # these weather are in a dict form [json]
        currentWeather  = client.getCurrentWeather(q = "Harare")                 # get current weather for Hre
        forecastWeather = client.getForecastWeather(q = "Harare", days = 7)     # get weather forecast for Hre
        return True, currentWeather, forecastWeather

    except ApixuException as e:
        return False, "[!] Error querying data {}".format(e.message)

def getOpenweathermap(ApiKey):
    '''
        get data from openweathermap.org site
        get current weather data and weather forecast
        used co-ordinates for my home time Triangle, Zimbabwe
        * we can use my city id as follows
          - response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?id=524901' ^ id = 'your city id'
        chiredzi [-21.05, 31.67]
    '''


    key = ApiKey
    weather_url  = 'http://api.openweathermap.org/data/2.5/weather?lat=-21.05&lon=31.67' + '&APPID=' + key
    forecast_url = 'http://api.openweathermap.org/data/2.5/forecast?lat=-21.05&lon=31.67' + '&APPID=' + key
    #res1 = req.urlopen(weather_url)
    res2 = req.urlopen(forecast_url)
    #output1 = res1.read().decode('utf-8')
    output2 = res2.read().decode('utf-8')
    #Opdata1 = json.loads(output1)
    Opdata2 = json.loads(output2)
    return True, Opdata2

# save data to file
try:
    if getOpenweathermap(OPENWEATHERMAP_KEY)[0]:
        ac, Opdata2 = getOpenweathermap(OPENWEATHERMAP_KEY)
        #print(Opdata1)
        print()
        print(Opdata2)

        '''
        with open("Current_op_weather.json", "w") as f:
            f.write(" -- CURRENT OP WEATHER DATA -- \n")
            f.write(str(Opdata1))
        '''


        with open("Forecast_op_weather.json", "w") as fl:
            fl.write(" -- FORECAST OP DATA -- \n")
            fl.write(Opdata2)


except Exception as e:
    print ("There was a problem saving to disk ", e)
