#!pip install -e "Z:\forni\Downloads\opensky-api-master\opensky-api-master\python"
#!pip install --upgrade google-cloud-storage
#!pip3 install flightradar24
#from opensky_api import OpenSkyApi
from google.cloud import storage
import sqlite3
import pandas as pd
import numpy as np
import mysql.connector
import flightradar24
import math
import requests

fr = flightradar24.Api()
#api = OpenSkyApi()
cnx = mysql.connector.connect(user='team', password='cs540', host='34.148.203.103', database= 'FlightDatabase')

def getICAOFromRegion(lat_min, lat_max, long_min, long_max):
    url = 'https://opensky-network.org/api/states/all?lamin='+lat_min+'&lomin='+long_min+'&lamax='+lat_max+'&lomax='+long_max
    response = requests.get(url)
    return response.json()


def getArivals(airport): #aiport example: 'DBA'
    #from 12pm to 1pm on Jan 29 2018 - from api documents
    url = 'https://USERNAME:PASSWORD@opensky-network.org/api/flights/arrival?airport='+airport+'&begin=1517227200&end=1517230800'
    response = requests.get(url)
    return response.json()

def getDepartures(airport): #aiport example: 'DBA'
    #from 12pm to 1pm on Jan 29 2018 - from api documents
    url = 'https://USERNAME:PASSWORD@opensky-network.org/api/flights/departure?airport='+airport+'&begin=1517227200&end=1517230800'
    response = requests.get(url)
    return response.json()


def findAirportLoc(name):
    #FlightRadar24
    dataAirport = fr.get_airports()
    listAirport= dataAirport['rows']
    for airport in listAirport:
        if(name in airport['name']):
            return airport['lat'], airport['lon']
        
def findLocRange(lat_center,long_center):
    #20km range
    range = 0.09
    lat_min = lat_center - range
    lat_max = lat_center + range
    long_min = long_center - (range/ math.cos(lat_center*math.pi/180))
    long_max = long_center + (range / math.cos(lat_center*math.pi/180))
    return lat_min,lat_max,long_min,long_max

def trackAircraft(icao):
    url = "https://USERNAME:PASSWORD@opensky-network.org/api/tracks/all?icao24="+icao+'&time=0'
    response = requests.get(url)
    return response.json()

lat_center, long_center = findAirportLoc('Daytona')
lat_min, lat_max, long_min, long_max = findLocRange(lat_center, long_center)
aircraftRegionData = getICAOFromRegion(str(lat_min), str(lat_max), str(long_min), str(long_max))

print(aircraftRegionData['states'][0][0])
tracker = trackAircraft(aircraftRegionData['states'][0][0])
