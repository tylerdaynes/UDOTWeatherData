# This file imports weather data from the Y drive to the same directory as main.py for analysis

import pandas as pd

xlpath = 'Y:/Environmental/ENV.Secure/Ambient Air Monitoring/Data/UDOT Weather Station/Just_Data.xlsm'
# Path to excel file

df = pd.read_excel(xlpath, sheet_name='Clean_Data', parse_dates=['Reading_Date_Time'])  # Read file
df.rename(columns={
    'Reading_Date_Time': 'Date_Time'
}, inplace=True)  # Rename the date time column
df = df.set_index('Date_Time')  # Set the index to Date Time column (keeps everything in order)
df.drop_duplicates(inplace=True)  # Remove duplicates

df.to_csv('WeatherData.csv', sep='\t')  # Save as CSV file
