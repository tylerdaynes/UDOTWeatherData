# This is a module for main.py that creates wind roses for the selected date range

from windrose import WindroseAxes
from matplotlib import pyplot as plt
from matplotlib import cm
from datetime import timedelta

if __name__ == '__main__':  # Prevents this module from running as a stand alone python script
    print('You need to run main.py for this script to work')
else:
    def create_wind_roses(currentdate, enddate, delta, df):  # function to create wind roses
        date_range = enddate - currentdate
        if date_range.days >= 20:
            print('More than 20 days in date range, skipping wind rose creation')
        else:
            print(f'Starting to make windroses for {currentdate:%m/%d/%Y}-{enddate:%m/%d/%Y}')
            while currentdate <= enddate:  # loop through each day in date range
                w_dir = df[currentdate: currentdate + delta].Wind_Direction  # select wind direction data
                w_speed = df[currentdate: currentdate + delta].Wind_Speed  # select wind w_speed data
                windrose = WindroseAxes.from_ax()  # create window for wind rose
                windrose.contourf(w_dir, w_speed, cmap=cm.autumn)  # Plot a filled contour map
                windrose.contour(w_dir, w_speed, colors='black', linewidth=1)
                # Plot an empty contour map on top of filled
                windrose.set_legend(title='Wind Speed Bins (mph)',
                                    loc='lower center',
                                    ncol=6,
                                    borderaxespad=-5)  # Set up the legend. borderaxespad = space between plot & legend
                windrose.set_title(f'{currentdate:%a, %b %d, %Y} Wind Rose')  # Set up title for each plot
                windrose.grid(color='black', linewidth=1)  # Make the grid black
                plt.savefig(f'WindRoses/{currentdate:%Y.%m.%d}_WindRose.png')  # save plot as PNG to WindRoses folder
                currentdate = currentdate + timedelta(days=1)  # Move the current date forward by 1

            plt.show()
