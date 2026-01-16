import pandas as pd
import json

json_file_path = '/home/hadoop/dakar_weather.json'
with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())

df = pd.DataFrame({ 
         'time' : contents['time'], 
         'temperature' : contents['temperature_2m'],
         'apparentTemperature' : contents['apparent_temperature'],
         'relativeHumidity' : contents['relativehumidity_2m'],
         'windSpeed' : contents['windspeed_10m'],
         'pressure' : contents['pressure_msl'],
         'weathercode': contents['weathercode'],
         'rain' : contents['rain']
})

df.to_csv("/home/hadoop/dakar_weather.csv",index=False)