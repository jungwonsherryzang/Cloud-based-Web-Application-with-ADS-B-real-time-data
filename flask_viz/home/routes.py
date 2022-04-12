# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
import folium
import os
import sys
from tabulate import tabulate
import pandas as pd
from signal import signal, SIGINT
from google.cloud import bigquery
bigquery_client = bigquery.Client()

def pop_data():
    query_job = bigquery_client.query(
        """
        SELECT
            * 
        FROM
            `cs540-project.Flights.AllData`
        """
    )
    # Handle query_job result and return to flask to display
    res = query_job.result().to_dataframe()
    cols={'icao24':'ICAO24', 'callsign':'Callsign','origin_country':'Origin',
            'longitude':'Lon','latitude':'Lat','baro_altitude':'Baro-Alt',
            'velocity':'Velocity','true_track':'True-Track',
            'vertical_rate':'Vert Rate','geo_altitude':'Geo-Alt',
            'time_position':'Time/Pos','last_contact':'Last Contact',
            'obs_time':'OBS Time','on_ground':'On Ground?'}
    df=pd.DataFrame(res).drop(columns=['spi']).rename(cols, axis=1)
    return(df)

@blueprint.route('/map')
def data_vis():
    df = pop_data()
    start_coords = (29.18, -81.05)
    flight_map = folium.Map(location=start_coords, zoom_start=11,min_zoom=8,max_zoom=14)
    icon_url='apps/static/assets/img/plane_icon.png'
    for i in range(0,len(df)):
        lat = df.loc[i]['Lat']
        lon = df.loc[i]['Lon']
        callsign = df.loc[i]['Callsign']
        new_icon = folium.features.CustomIcon(icon_url, icon_size=(16,16), icon_anchor=('center'))
        folium.Marker([lat, lon], popup=callsign, icon=new_icon).add_to(flight_map)
    return flight_map._repr_html_()

@blueprint.route('/index.html')
@login_required
def index():
    df = pop_data()
    tables = [df.to_html(index=False, classes='display table table-striped table-hover', border=0, table_id='basic-datatables', header=True)]
    return render_template('home/index.html', segment='index', tables=tables)

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None


'''@blueprint.route('/index')
def database():
    print('Hello World!')
    query_job = bigquery_client.query(
        """
        SELECT
            * 
        FROM
            `cs540-project.Flights.AllData`
        """
    )
    # Handle query_job result and return to flask to display
    res = query_job.result().to_dataframe()
    output = tabulate(res, headers='keys', tablefmt='psql')
    return render_template('home/index.html', message=output)'''