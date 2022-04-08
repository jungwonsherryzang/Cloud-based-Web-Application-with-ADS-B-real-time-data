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
          * 
        FROM 
          `cs540-project.Flights.AllData`
        """
    )
    # Handle query_job result and return to flask to display
    res = query_job.result().to_dataframe()
    #print(res, file=sys.stderr)
    #print(res)
    
#    for row in res:
#        output = "entries: " + str(row)



    output = tabulate(res, headers='keys', tablefmt='psql')

   
    return render_template('index.html', message=output)

if __name__ == '__main__':
    signal(SIGINT, handler)
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
