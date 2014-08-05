#plots all Tuesdays(or other day of week) of a certain month on same plot

import os
import pandas as pd
import MySQLdb as sqd
import pandas.io.sql as sql
import matplotlib.pyplot as plt

#set up directory and database connection
os.chdir('/Users/durango/PycharmProjects/Energy Project')
mydb = sqd.connect(host = '127.0.0.1', user = 'root', db = 'rdcep_amanda')

def plot_DOW (month, DOW):

    #make dataframe from query    
    df = sql.read_frame('select * from all_avg where dayname(date) = "' + DOW + '" and date between "' +
                        month + '-01" and "' + month + '-28"', mydb, parse_dates = ['date'], index_col = ['date', 'time'])

    #convert values to float
    df[['total_energy']] = df[['total_energy']].astype(float)

    #pivot table so dates are on x-axis and columns are named correctly
    df = df.unstack(level=-2)
    df.columns = df.columns.droplevel(level=0)
    df.columns = pd.DatetimeIndex(df.columns).date

    #make the plot
    plot = df.plot(figsize = (12,8))
    plot.set_xlabel('Time', fontsize = 14)
    plot.set_ylabel('Energy Consumption in kW/h', fontsize = 14)
    plot.set_title('Time vs. Energy Consumption ' + month + ' ' + DOW, fontsize = 18)
    plt.savefig('/Users/durango/Desktop/RDCEP_Energy/weekday_linegraphs/' + month + '_' + DOW, dpi=100)


months_31 = ['2013-05', '2013-07', '2013-08','2013-10', '2013-12', '2014-01', '2014-03']
months_30 = ['2013-04', '2013-06', '2013-09','2013-11', '2014-04']

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for month in months_30:
    for day in days:
        try:
            plot_DOW(month, day)
        except ValueError:
            print month
            print day

for day in days:
    plot_DOW('2014-04', day)

#error:
#2013-10
#Sunday
#2013-10
#Monday
#2013-10
#Tuesday
#2013-10
#Wednesday
#2013-10
#Thursday
#2013-10
#Friday
#2013-10
#Saturday


