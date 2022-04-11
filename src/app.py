import os
import sys
from tabulate import tabulate

from signal import signal, SIGINT
from flask import Flask, render_template

from google.cloud import bigquery
bigquery_client = bigquery.Client()

def handler(signal_received, frame):
    # SIGINT or  ctrl-C detected, exit without error
    exit(0)

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a simple HTML page with a friendly message."""
    query_job = bigquery_client.query(
        """
        SELECT 
          callsign, longitude, latitude, velocity 
        FROM 
          `cs540-project.Flights.AllData`
        WHERE
            `callsign` LIKE 'ERU%' 
        """
    )
    # Handle query_job result and return to flask to display
    res = query_job.result().to_dataframe()
    res = res.to_html().replace('<table border="1"', '<table border="1" align="center"')
    return render_template('index.html', message = res) #pass result to message
    #print(res, file=sys.stderr)
    #print(res)
    
#    for row in res:
#        output = "entries: " + str(row)

    #output = tabulate(res, headers='keys', tablefmt='psql')
