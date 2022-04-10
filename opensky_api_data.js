//RETRIEVING DATA FROM REST API
const { text } = require('body-parser');
const { stringify } = require('querystring');
const file = require('./1_file.js');
const request = require('request-promise'); //calling library

const url = "https://opensky-network.org/api/states/all"; //URL to access the REST API

request.get(url) //performs an HTTP GET request to the REST API
    .then(response => { //handles the response; this is the data that is returned from the REST API
        console.log(response);
    })
    .catch(err => { //handles any error that might occur
        console.error(err);
    });

    
//FUNCTION TO IMPORT JSON DATA FROM A REST API
function importJsonFromRestApi (url) { //making a function to import JSON data from a REST APT
    return request.get(url) //uses HTTP GET to pull data from the REST API
        .then(response => {
            return JSON.parse(response);
        });
};
module.exports = importJsonFromRestApi;



//FUNCTION TO EXPORT DATA TO A JSON TEXT FILE(JSON STRING)
function exportJsonFile (fileName, data) { //making a function to export a JSON file
    const json = JSON.stringify(data, null, 4); //JSON.stringify to convert to JSON text(string)
    return file.write(fileName, json); //using write function to write the JSON data to the filesystem
};
module.exports = exportJsonFile;


importJsonFromRestApi("https://opensky-network.org/api/states/all")
    .then(data => exportJsonFile("./output/opensky.json", data))
    .catch(err => {
        console.error("An error occured!");
        console.error(err.stack);
    });