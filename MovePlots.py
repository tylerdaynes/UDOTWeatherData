# This file exports the plots created from main.py to the Y drive

import os
import shutil

NewWeatherPath = 'Y:/Environmental/ENV.Secure/Ambient Air Monitoring/Data/UDOT Weather Station/Weather_Plots'
NewWindPath = 'Y:/Environmental/ENV.Secure/Ambient Air Monitoring/Data/UDOT Weather Station/Wind_Roses'

for entry in os.scandir('./WeatherPlots'):  # Iterate through directory
    if entry.path.endswith('.png'):  # Check if file is a PNG
        shutil.move(entry.path, f'{NewWeatherPath}/{entry.name}')  # Move file to Y Drive
        print(f'Moved {entry.name} to Y Drive')


for entry in os.scandir('./WindRoses'):  # Iterate through directory
    if entry.path.endswith('.png'):  # Check if file is a PNG
        shutil.move(entry.path, f'{NewWindPath}/{entry.name}')  # Move file to Y Drive
        print(f'Moved {entry.name} to Y Drive')
