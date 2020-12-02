# This is the main script to analyze UDOT weather data

import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from tkcalendar import DateEntry
import Read_Data as rd  # Import the Read_Data.py script
import Plots  # Import the Plots.py script
import WindRoses  # Import the WindRoses.py script

end = rd.df.last_valid_index()  # Find the last time of recording
end_day = end.day  # day of the last time of recording
end_month = end.month  # month of the last time of recording
end_year = end.year  # year of the last time of recording

start = end - timedelta(days=7)  # 1 week before the last time of recording
start_day = start.day
start_month = start.month
start_year = start.year

delta = timedelta(hours=23, minutes=59)  # time difference for Wind Roses and single date analysis


def date_entry():  # function for button
    date_entry.StartDate = datetime.strptime(d1.get(), '%m/%d/%y')  # get the start date
    date_entry.EndDate = datetime.strptime(d2.get(), '%m/%d/%y')  # get the end date
    root.destroy()  # close the popup window


root = tk.Tk()  # create the popup window
root.title('Date Range')  # title for the popup window

label0 = ttk.Label(root, text=f'Choose the date range for analysis\nDefault is one week from last recorded value')
# top center text
label0.grid(row=0, columnspan=2)  # placement of top center text

label1 = ttk.Label(root, text='Start Date:')  # middle left text
label1.grid(row=1, column=0, pady=5)  # placement of middle left text

label2 = ttk.Label(root, text='End Date:')  # bottom left text
label2.grid(row=2, column=0)  # placement of bottom left text

d1 = DateEntry(root, day=start_day, month=start_month, year=start_year)  # start date field
d1.grid(row=1, column=1, pady=5)  # placement of start date field

d2 = DateEntry(root, day=end_day, month=end_month, year=end_year)  # date date field
d2.grid(row=2, column=1)  # placement of end date field

btn1 = ttk.Button(root, text='Finish', command=date_entry)  # Finish button
btn1.grid(row=3, columnspan=2, pady=5)  # placement of button

root.mainloop()  # start the popup window

startdate = date_entry.StartDate  # retrieve the start date from the popup
enddate = date_entry.EndDate  # retrieve the date date from the popup
enddate = enddate + delta  # Adjust the enddate to pull values for entire day

print(f'Start Date: {startdate}\nEnd Date: {enddate}')

index = rd.range(startdate, enddate)  # read in the index from the Read_Data.py data frame
air_temp = rd.airtemp(startdate, enddate)  # read the Air Temperature data from the data frame
humidity = rd.humid(startdate, enddate)  # read the humidity data from the data frame
wind_speed = rd.windspeed(startdate, enddate)  # read the wind w_speed data from the data frame
precipitation = rd.precip(startdate, enddate)  # read the precipitation data from the data frame
pressure = rd.pres(startdate, enddate)  # read the pressure data from the data frame


Plots.create_plots(index=index,
                   air_temp=air_temp,
                   humidity=humidity,
                   windspeed=wind_speed,
                   precipitaion=precipitation,
                   pressure=pressure,
                   startdate=startdate,
                   enddate=enddate)

currentdate = startdate  # Set iterable date for wind rose creation

WindRoses.create_wind_roses(currentdate=currentdate,
                            enddate=enddate,
                            delta=delta,
                            df=rd.df)
