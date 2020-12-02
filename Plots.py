# This is a module for main.py that creates and saves plots for several weather parameters over the selected date range

from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

if __name__ == '__main__':  # Prevents this module from running as a stand alone python script
    print('You need to run main.py for this script to work')
else:
    plt.style.use('seaborn-whitegrid')  # Set preferred plot style

    locator = mpl_dates.AutoDateLocator()  # Format tick marks for dates

    formatter = mpl_dates.ConciseDateFormatter(locator)  # Automatically adjust ticks for best fit
    formatter.formats = ['%y',      # If ticks are mostly years (yy)
                         '%b',      # If ticks are mostly months (mon)
                         '%d',      # If ticks are mostly days (dd)
                         '%H:%M',   # If ticks are mostly hours  (hh:mm)
                         '%H:%M',   # If ticks are mostly minutes  (hh:mm)
                         '%s.%f'    # If ticks are mostly seconds (ss.micro)
                         ]   # Formats for tick labels
    formatter.zero_formats = [''] + formatter.formats[:-1]  # Formatting for zero values
    formatter.zero_formats[3] = '%d-%b'  # If ticks are hours, then zero ticks are (dd-mon)
    formatter.offset_formats = ['',                 # Blank if limits are years
                                '%Y',               # If limits are months (yyyy)
                                '%b %Y',            # If limits are days (mon yyyy)
                                '%b %Y',            # If limits are hours (mon yyyy)
                                '%d %b %Y',         # If limits are minutes (dd mon yyyy)
                                '%d %b %Y %H:%M'    # If limits are seconds (dd mon yyyy hh:mm)
                                ]   # Formats for bottom right label


    def create_plots(index,
                    air_temp,
                    humidity,
                    windspeed,
                    precipitaion,
                    pressure,
                    startdate,
                    enddate):   # function to create weather plots

        start_day = startdate.day
        start_month = startdate.month
        start_year = startdate.year
        checkstart = start_day + start_month + start_year  # Pull just the date from the startdate variable

        end_day = enddate.day
        end_month = enddate.month
        end_year = enddate.year
        checkend = end_day + end_month + end_year  # Pull just the date from the enddate variable

        fig1, (temp, humid) = plt.subplots(nrows=2, sharex=True)  # create window for temperature and humidity plot
        temp.plot(index, air_temp)  # plot temperature data
        temp.set(title='Air Temperature & Relative Humidity',
                 ylabel='Temperature (\N{DEGREE SIGN}F)')  # set chart title and y-axis label
        humid.plot(index, humidity)  # plot humidity data
        humid.set(ylabel='Relative Humidity (%)')  # set y-axis label
        humid.xaxis.set_major_locator(locator)  # format x-axis tick marks
        humid.xaxis.set_major_formatter(formatter)  # format date time axis labels
        plt.tight_layout()  # Fit plots to window

        if checkend == checkstart:  # Check if the start date and end date are the same
            plt.savefig(f'WeatherPlots/{startdate:%Y.%m.%d}_Temp_RH.png')  # save plot as PNG in WeatherPlots folder
        else:
            plt.savefig(f'WeatherPlots/{startdate:%Y.%m.%d}-{enddate:%Y.%m.%d}_Temp_RH.png')

        fig2, wind = plt.subplots()  # create window for wind plot
        wind.plot(index, windspeed)  # plot wind w_speed data
        wind.set(title='Average Wind Speed',
                 ylabel='Wind Speed (mph)')  # set title and y-axis label
        wind.xaxis.set_major_locator(locator)  # format x-axis tick marks
        wind.xaxis.set_major_formatter(formatter)  # format date time axis labels
        plt.tight_layout()  # Fit plots to window

        if checkend == checkstart:
            plt.savefig(f'Weatherplots/{startdate:%Y.%m.%d}_WindSpeed.png')  # save plot as PNG in WeatherPlots folder
        else:
            plt.savefig(f'Weatherplots/{startdate:%Y.%m.%d}-{enddate:%Y.%m.%d}_WindSpeed.png')

        fig3, precip = plt.subplots()  # create window for precipitation plot
        precip.plot(index, precipitaion)  # Plot Precipitation data
        precip.fill_between(index, precipitaion)  # Fill below line to X-Axis
        precip.set(title='Accumulated Precipitation',
                   ylabel='Accumulated Precipitation (in)')  # Set titles
        precip.xaxis.set_major_locator(locator)  # format x-axis tick marks
        precip.xaxis.set_major_formatter(formatter)  # format date time axis labels
        plt.tight_layout()  # Fit plots to window

        if checkend == checkstart:
            plt.savefig(f'WeatherPlots/{startdate:%Y.%m.%d}_Precip.png')  # save plot as PNG in WeatherPlots folder
        else:
            plt.savefig(f'WeatherPlots/{startdate:%Y.%m.%d}-{enddate:%Y.%m.%d}_Precip.png')

        fig4, pressure_fig = plt.subplots()  # Set up plot for Pressure
        pressure_fig.plot(index, pressure)  # Plot Pressure data
        pressure_fig.set(title='Atmospheric Pressure',
                         ylabel='Pressure (in Hg)')  # Set titles
        pressure_fig.xaxis.set_major_locator(locator)  # format x-axis tick marks
        pressure_fig.xaxis.set_major_formatter(formatter)  # format date time axis labels
        plt.tight_layout()  # Fit plots to window

        if checkend == checkstart:
            plt.savefig(f'WeatherPlots/{startdate:%Y.%m.%d}_Pressure.png')  # save plot as PNG in WeatherPlots folder
        else:
            plt.savefig(f'WeatherPlots/{startdate:%Y.%m.%d}-{enddate:%Y.%m.%d}_Pressure.png')

        plt.show()  # Show plots
