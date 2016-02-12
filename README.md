# nicholas-gibson-web-services

This repository contains the code for a web service which finds information about the ten current "hottest" deals at Argos on the site HotUKDeals. The web service will compare the prices of these products with those of a fictional competitor and return information in JSON about these products, ordered in order of the greatest price difference between the price at Argos and the price of the competitor.

This is a "live" service which will always have the most up-to-date information from HotUKDeals.

This repository also contains code for a web page which uses this JSON information and displays a table containing information about the ten "hottest" Argos products, including the title, description, argos price, competitor's price, the price difference, the temperature, an image of the product and links to the HotUKDeals page and to the Argos page.

This was written using Python 2.7 and the web.py web framework.

<b> Notable files: </b> <br>
start.py <br>
JsonService.py - contains the code for the JSON web service <br>
Table.py - contains the code for the web page visually displaying product information <br>
templates/webpage.html - the html file for the web page <br>

<b> How to run the services: </b> <br>
If Python 2.7 is not installed, it will need to be installed. Python 2.7.11 can be downloaded from https://www.python.org/. This project has been tested using Python 2.7.8 and Python 2.7.11, but it may work using other Python versions.

Run start.py in python to start the web server. <br> You could do this by double click run.bat to start the webserver on your computer. You may need to add python to your path environment variable. Alternatively run <br>
  <i> &emsp; &emsp; python start.py </i> <br>
from the command line.

The server should now be running. In your web browser (tested on Internet explorer, chrome and firefox) visit http://localhost:8080/json to see the json service and http://localhost:8080/table to see a webpage displaying the results in a visual format.

![alt tag](https://raw.githubusercontent.com/nicholasgibson/nicholas-gibson-web-services/master/table.png)
<br><br>
![alt tag](https://raw.githubusercontent.com/nicholasgibson/nicholas-gibson-web-services/master/json.png)

