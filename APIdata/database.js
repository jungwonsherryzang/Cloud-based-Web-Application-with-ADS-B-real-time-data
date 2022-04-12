from google.cloud import bigquery
import mysql.connector
import pandas as pd
import json
import flightradar24
import requests
import math
import os
from datetime import datetime
import geopandas as gpd
import geoplot as gplt
import folium
from branca.element import Figure
fr = fr = flightradar24.Api()

//Airport information
def findAirportLoc(name):
    #FlightRadar24
    dataAirport = fr.get_airports()
    listAirport= dataAirport['rows']
    for airport in listAirport:
        if(name in airport['name']):
            return airport['lat'], airport['lon']

//Setting distance around the airport
def findLocRange(lat_center,long_center):
    #20km range
    range = 0.09
    lat_min = lat_center - range
    lat_max = lat_center + range
    long_min = long_center - (range/ math.cos(lat_center*math.pi/180))
    long_max = long_center + (range / math.cos(lat_center*math.pi/180))
    return lat_min,lat_max,long_min,long_max

//Query data
def collectData(lat_min, lat_max, long_min, long_max):
    r = requests.get('https://opensky-network.org/api/states/all?lamin='+lat_min+'&lomin='+long_min+'&lamax='+lat_max+'&lomax='+long_max)
    r.status_code
    file=r.json()

    df=pd.DataFrame(file['states'],columns=['icao24', 'callsign','origin_country','time_position','last_contact',
                                            'longitude','latitude','baro_altitude','on_ground','velocity',
                                            'true_track','vertical_rate','sensors','geo_altitude','squawk','spi','x','y']).drop(columns=['x','y']).assign(obs_time= lambda x: file['time'])
    df[['time_position','last_contact','obs_time']] = df[['time_position','last_contact','obs_time']].apply(pd.to_datetime, unit='s')
    #df.set_index(['obs_time', 'callsign'],inplace=True)
    return df


//cleaning dataframe
def cleanDataframe(df):
    df = df.drop(columns=['sensors','squawk'])
    df = df.where(pd.notnull(df), None)
    df = df.reset_index(drop=True)
    return df


//pushing cleaned datafroma to cloud
def connectQuery(df):
    credentials = r'https://github.com/jungwonsherryzang/Cloud-based-Web-Application-with-ADS-B-real-time-data/blob/main/cs540-project-key.json'
    os.environ['Google_APPLICATION_CREDENTIALS'] = credentials
    client = bigquery.Client()
    table_id = 'cs540-project.Flights.AllData'
    df = df.to_gbq(table_id , if_exists='append')


//Interative map
def main():
    
    lat_center, long_center = findAirportLoc('Daytona')
    lat_min, lat_max, long_min, long_max = findLocRange(lat_center, long_center)
    df = collectData(str(lat_min), str(lat_max), str(long_min), str(long_max))
    df = cleanDataframe(df)
    #connectQuery(df)
    return(df)
    
adsb_df = main()
adsb_df
