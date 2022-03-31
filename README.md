# Cloud-Based Web Application for Real-Time Flight Information
Embry Riddle Aeronautical University CS540 Semester Project


In our view, our project proposes combining the database management with the integration of cloud computing techniques. The goal of this project is to extract real-time flight data, including flight number, airline name, flight departure/arrival time, departure/arrival airport and flight status and to share the extracted flight information to web using cloud computing. In this work, OpenSky provides the real-time flight information and global aviation data Application Programming Interface (API). The data from OpenSky is sent in a JSON data format to a Python architecture system that cleans and stores the data in a cloud-based server in order to be retrieved and displayed on a web hosting server. This work shows that combination the error-free real-time flight data and cloud computing can help travelers be more aware of changes in their travel arrangements such as flight delay or cancellations. 


# PYTHON API
It depends of the python-requests library http://docs.python-requests.org/

# INSTALLATION
``` python
sudo python setup.py install
```

or with pip
``` python
pip install -e /path/to/repository/python
```

## USAGE
``` python
from opensky_api import OpenSkyApi
api = OpenSkyApi()
s = api.get_states()
print(s)
```



