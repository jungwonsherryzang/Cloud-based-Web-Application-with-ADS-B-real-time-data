# Cloud-Based Web Application for Real-Time Flight Information
Embry Riddle Aeronautical University CS540 Semester Project


In our view, our project proposes combining the database management with the integration of cloud computing techniques. The goal of this project is to extract real-time flight data, including flight number, airline name, flight departure/arrival time, departure/arrival airport and flight status and to share the extracted flight information to web using cloud computing. In this work, OpenSky provides the real-time flight information and global aviation data Application Programming Interface (API). The data from OpenSky is sent in a JSON data format to a Python architecture system that cleans and stores the data in a cloud-based server in order to be retrieved and displayed on a web hosting server. This work shows that combination the error-free real-time flight data and cloud computing can help travelers be more aware of changes in their travel arrangements such as flight delay or cancellations. 

# DATA CLEANING
Using Python and Pandas for data cleaning is available: 
https://colab.research.google.com/drive/12wkrpM6ncUQMGkt5HSJbrQJqc7NhwbOc#scrollTo=L9cWrA6lL62G

<img width="919" alt="스크린샷 2022-04-10 오후 9 50 08" src="https://user-images.githubusercontent.com/91277856/162651912-d2d094de-fea8-49fe-9d47-a454456727b5.png">

## REAL-TIME DAYTONA BEACH AIRPORT MAP
<img width="556" alt="스크린샷 2022-04-10 오후 9 51 54" src="https://user-images.githubusercontent.com/91277856/162651994-6aa71c46-8967-4a4f-be3d-278082aedb8c.png">




# BIGQUERY

## PYTHON API WITH BIGQUERY
It depends of the python-requests library http://docs.python-requests.org/

## PYTHON AND FLASK INSTALLATION 
``` python
sudo python setup.py install
```
``` python
pip3 install flask
```

## BIGQUERY SERVER CONNECTION
This is the testing query data from out dataset that currently flying Embry Riddle aircraft
``` SQL
SELECT callsign, longitude, latitude, velocity
FROM 'cs540-project.Flights.AllData'
WHERE callsign LIKE 'ERU%'
```

## OUTCOME OF BIGQUERY SERVER CONNECTION AND EXPORTING QUERY
<img width="1221" alt="BigQuery server" src="https://user-images.githubusercontent.com/91277856/162801455-5e1168fb-8364-475c-8dc7-3f3855036c35.png">

