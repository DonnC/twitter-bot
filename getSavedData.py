import json
import time
import sys
from pprint import pprint

def getOWM(fhand):
    ''' get the data from the saved json file'''
    fname = fhand
    with open(fname) as f:
        fobj = f.read()
        fjson = json.loads(fobj)


    city   = fjson["city"]["name"]
    popltn = fjson["city"]["population"]
    data   = fjson["list"]
    return city, popltn, data

fhandler = 'forecast.json'
cityName, pop, w = getOWM(fhandler)
print("City name: ", cityName)
print("Population {} people".format(pop))
count   = 1
weather = []

for key in range(len(w)):
    Time = time.ctime(w[key]['dt'])
    temp = round(w[key]['main']['temp'] - 273.00, 2)
    hum  = w[key]['main']['humidity']
    desc = w[key]['weather'][0]['description']

    details = '''
    *Report #{}
    *Date time: {}
    -- today's main weather condition for #{}--
    Temp  : {}*C
    Hum   : {}%
    desc  : {} 
    #python #twimbos #IoT #twitterbot @donix_22
    '''.format(count, Time, 'Chiredzi', temp, hum, desc)

    weather.append(details)
    count += 1


