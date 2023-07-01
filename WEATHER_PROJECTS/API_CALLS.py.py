# Databricks notebook source
import requests
import json
import time

accessKey = "a9470153fe79424f9da35123230107"
header = {
    "Content-Type": "application/json"
}
_time = "_" + str(round(time.time()*1000))
targetFolder = "/mnt/output/Weather_Raw/"

cities = "london"
for city in cities:
    weatherBaseURL = \
        f"http://api.weatherapi.com/v1/current.json?key=a9470153fe79424f9da35123230107&q=London&aqi=yes"
    response = requests.get(url = weatherBaseURL, headers = header)
    data = response.json()
    fileName = city + _time + ".json"
    dbutils.fs.put(targetFolder + fileName, str(data), True) 

# COMMAND ----------

# MAGIC %fs ls 
# MAGIC dbfs:/mnt/output/Weather_Raw/d_1688184324899.json

# COMMAND ----------


