# Cloud-Based Web Application for Real-Time Flight Information
Embry Riddle Aeronautical University CS540 Semester Project


In our view, our project proposes combining the database management with the integration of cloud computing techniques. The goal of this project is to extract real-time flight data, including flight number, airline name, flight departure/arrival time, departure/arrival airport and flight status and to share the extracted flight information to web using cloud computing. In this work, OpenSky provides the real-time flight information and global aviation data Application Programming Interface (API). The data from OpenSky is sent in a JSON data format to a Python architecture system that cleans and stores the data in a cloud-based server in order to be retrieved and displayed on a web hosting server. This work shows that combination the error-free real-time flight data and cloud computing can help travelers be more aware of changes in their travel arrangements such as flight delay or cancellations. 


# PYTHON API WITH BIGQUERY
It depends of the python-requests library http://docs.python-requests.org/

# PYTHON INSTALLATION
``` python
sudo python setup.py install
```

or with pip
``` python
pip install -e /path/to/repository/python
```

## FETCHING DATA FROM REST API JAVASCRIPT USAGE
``` javascript
//FUNCTION TO IMPORT JSON DATA FROM A REST API
function importJsonFromRestApi (url) { 
    return request.get(url) 
        .then(response => {
            return JSON.parse(response);
        });
};
module.exports = importJsonFromRestApi;


//FUNCTION TO EXPORT DATA TO A JSON TEXT FILE(JSON STRING)
function exportJsonFile (fileName, data) { 
    const json = JSON.stringify(data, null, 4); 
    return file.write(fileName, json);
};
module.exports = exportJsonFile;
```
## FETCHED OPENSKY DATA EXAMPLE
``` json
{
    "time": 1649623672,
    "states": [
        [
            "4b1815",
            "SWR24KT ",
            "Switzerland",
            1649623672,
            1649623672,
            8.412,
            47.2735,
            4236.72,
            false,
            172.75,
            53.23,
            -8.13,
            null,
            4320.54,
            "2321",
            false,
            0
        ],
```


