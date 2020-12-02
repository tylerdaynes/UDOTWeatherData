IF YOU ARE SETTING UP THE PROJECT FOR THE FIRST TIME:
    1. If you are using PyCharm, create a new project on your computer
        file-> new project
        You can name it whatever you want, but you should keep it on the C drive so analysis can be done offline
    2. Copy the required files to the new project directory (not the venv):
        a. Plots.py
        b. Read_Data.py
        c. WindRoses.py
        d. XL2CSV.py
        e. MovePlots.py
        f. readme.txt
    3. Install the following packages using "pip install x" in the terminal
        a. pandas
        b. tkcalendar
        c. matplotlib
        d. windrose
            you may need to install the developer version for it to work
            (pip install git+https://github.com/python-windrose/windrose)
    4.  Create two folders for the plots to save into:
        a. WeatherPlots
        b. WindRoses
        These should be in the same directory as the python scripts

How to use main.py to analyze UDOT weather data:
    1.  Make sure all of the required files are in the same directory as main.py
        a. Plots.py
        b. Read_Data.py
        c. WindRoses.py
        d. WeatherPlots folder
        e. WindRoses folder
        f. XL2CSV.py
            not required for main.py to run
        g. MovePlots.py
            not required for main.py to run
        h. readme.txt
    2.  Run XL2CSV.py
        This will create a csv file to use when offline
        It uses the file 'Just_Data.xlsm' from the UDOT Weather Station folder on the Y drive
        Does not need to be run multiple times, unless loading new data from 'Just_Data.xlsm'
    3.  Run main.py
        Do this by going to Run-> Run... in PyCharm
            or by doing Alt+Shift+F10
        Running any of the modules will not work, they have to be run through main.py

    This will create and save plots for the following over the selected time period:
        1. Air Temperature & Relative Humidity
        2. Average Wind Speed
        3. Accumulated Precipitation
        4. Gauge Pressure
        5. Wind Roses for every day

    You can then run MovePlots.py to move the created plots to the Y drive
        This is done manually so analysis can be done offline