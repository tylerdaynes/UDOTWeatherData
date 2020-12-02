# This is a module for main.py that reads the weather data from WeatherData.csv

import pandas as pd

if __name__ == '__main__':  # Prevents this module from running as a stand alone python script
    print('You need to run main.py for this script to work')
else:
    df = pd.read_csv('WeatherData.csv',
                     sep='\t',
                     parse_dates=['Date_Time'],
                     index_col='Date_Time')  # create data frame from CSV file

    df_hour = df.resample('H').mean()  # resample data for hourly average


    def range(startdate, enddate):  # Load the date range to memory
        x = df_hour[startdate: enddate].index  # X-Axis values
        print('Date Range loaded')
        return x


    def airtemp(startdate, enddate):  # load the air temperature data to memory
        AirTemp = df_hour[startdate: enddate].Air_Temperature  # Air temperature
        print('Air Temperature Loaded')
        return AirTemp


    def humid(startdate, enddate):  # load the relative humidity data to memory
        RH = df_hour[startdate: enddate].Relative_Humidity  # Humidity
        print('Relative Humidity Loaded')
        return RH


    def windspeed(startdate, enddate):  # load the wind w_speed data to memory
        w_speed = df_hour[startdate: enddate].Wind_Speed  # Average Wind Speed
        print('Wind Speed Loaded')
        return w_speed


    def precip(startdate, enddate):  # load the precipitation data to memory
        Acc_Precip = df_hour[startdate: enddate].Precipitation_Accumulated_24_hr  # Precipitation over 24 hr
        print('Precipitation Loaded')
        return Acc_Precip


    def pres(startdate, enddate):  # load the pressure data to memory
        pressure = df_hour[startdate: enddate].Pressure  # Gauge pressure
        print('Pressure Loaded')
        return pressure
