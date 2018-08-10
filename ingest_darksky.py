#!/usr/bin/env python

import time
import datetime
import pprint
import os
import json
import requests
from influxdb import InfluxDBClient

# Set the variables from , influxDB should be localhost on Pi
host = "localhost"
port = 8086
user = os.environ['influx_user']
password = os.environ['influx_pass']
apikey = os.environ['apikey']
dbname = os.environ['influx_db']
lat = os.environ['lat']
longitude = os.environ['longitude']
now = datetime.datetime.now()

# Make the call
url = 'https://api.darksky.net/forecast/' + apikey + '/' + lat + ',' + longitude + '?units=si'
response = requests.get(url)
json = json.loads(response.text)

# Extract values
precipProb           = json["currently"]["precipProbability"]
temperature          = json["currently"]["temperature"]
apparent_temperature = json["currently"]["apparentTemperature"]
dewPoint             = json["currently"]["dewPoint"]
humidity             = json["currently"]["humidity"]
windSpeed            = json["currently"]["windSpeed"]
windGust             = json["currently"]["windGust"]
windBearing          = json["currently"]["windBearing"]
visibility           = json["currently"]["visibility"]
cloudCover           = json["currently"]["cloudCover"]
pressure             = json["currently"]["pressure"]
ozone                = json["currently"]["ozone"]
uvIndex              = json["currently"]["uvIndex"]

# Create the InfluxDB object
myclient = InfluxDBClient(host, port, user, password, dbname)

iso = time.ctime()

# Write the values to the db
float_precipProb = float(precipProb)
json_precip_prob = [
    {
      "measurement": "precipProb",
      "tags": {
        "temp": "precipProb"
        },
      "time": iso,
      "fields": {
        "value": float_precipProb
        }
    }
]

myclient.write_points(json_precip_prob)

json_temp = [
    {
      "measurement": "temperature",
      "tags": {
        "temp": "temperature"
        },
      "time": iso,
      "fields": {
        "value": temperature
        }
    }
]

myclient.write_points(json_temp)

json_app_temp = [
    {
      "measurement": "apparent temperature",
      "tags": {
        "temp": "apparent temperature"
        },
      "time": iso,
      "fields": {
        "value": apparent_temperature
        }
    }
]

## Write JSON to InfluxDB
myclient.write_points(json_app_temp)

json_dew_point = [
    {
      "measurement": "dew point",
      "tags": {
        "temp": "dew point"
        },
      "time": iso,
      "fields": {
        "value": dewPoint
        }
    }
]

json_humidity = [
    {
      "measurement": "humidity",
      "tags": {
        "temp": "humidity"
        },
      "time": iso,
      "fields": {
        "value": humidity
        }
    }
]

myclient.write_points(json_humidity)

json_windSpeed = [
    {
      "measurement": "windSpeed",
      "tags": {
        "temp": "windspeed"
        },
      "time": iso,
      "fields": {
        "value": windSpeed
        }
    }
]

myclient.write_points(json_windSpeed)

float_windGust = float(windGust)
json_windGust = [
    {
      "measurement": "windGust",
      "tags": {
        "temp": "windGust"
        },
      "time": iso,
      "fields": {
        "value": float_windGust
        }
    }
]

myclient.write_points(json_windGust)

json_windBearing = [
    {
      "measurement": "windBearing",
      "tags": {
        "temp": "windBearing"
        },
      "time": iso,
      "fields": {
        "value": windBearing
        }
    }
]

myclient.write_points(json_windBearing)

json_visibility = [
    {
      "measurement": "visibility",
      "tags": {
        "temp": "visibility"
        },
      "time": iso,
      "fields": {
        "value": visibility
        }
    }
]

myclient.write_points(json_visibility)

json_cloudCover = [
    {
      "measurement": "cloudCover",
      "tags": {
        "temp": "cloudCover"
        },
      "time": iso,
      "fields": {
        "value": cloudCover
        }
    }
]

myclient.write_points(json_cloudCover)

json_pressure = [
    {
      "measurement": "pressure",
      "tags": {
        "temp": "pressure"
        },
      "time": iso,
      "fields": {
        "value": pressure
        }
    }
]

myclient.write_points(json_pressure)


json_ozone = [
    {
      "measurement": "ozone",
      "tags": {
        "temp": "ozone"
        },
      "time": iso,
      "fields": {
        "value": ozone
        }
    }
]

myclient.write_points(json_ozone)



json_uvIndex = [
    {
      "measurement": "uvIndex",
      "tags": {
        "temp": "uvIndex"
        },
      "time": iso,
      "fields": {
        "value": uvIndex
        }
    }
]

myclient.write_points(json_uvIndex)
