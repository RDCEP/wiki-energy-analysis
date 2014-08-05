#plot average Sunday, Monday, Tuesday, Wednesday... for one month on the same plot

import os
import pandas as pd
import MySQLdb as sqd
import pandas.io.sql as sql
import matplotlib.pyplot as plt

#set up directory and database connection
os.chdir('/Users/durango/PycharmProjects/Energy Project')
mydb = sqd.connect(host = '127.0.0.1', user = 'root', db = 'rdcep_amanda')


def plot_dow_overlay(month):
    
    #create dataframe from query
    df = sql.read_frame('select * from all_avg_dt where datetime between "' + month + '-01 00:00:00" and "' + month + '-31 23:45:00"',
                    mydb, parse_dates = ['datetime'], index_col = ['datetime'])

    df[['total_energy']] = df[['total_energy']].astype(float)

    #compute average day of week
    df = df.groupby((df.index.dayofweek, df.index.time)).mean()

    #rearrange table so day of week is on x-axis and columns are named correctly
    df = df.unstack(level=-2)
    df.columns = df.columns.droplevel(level=0)
    df.columns = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    #make the plot
    plot = df.plot(figsize = (12,8))
    plot.set_xlabel('Time', fontsize = 14)
    plot.set_ylabel('Energy Consumption in kW/h', fontsize = 14)
    plot.set_title('Time vs. Energy Consumption ' + month, fontsize = 18)
    plt.savefig('/Users/durango/Desktop/RDCEP_Energy/weekday_overlay_linegraphs/' + month , dpi=100)

months = ['2013-04', '2013-05', '2013-06', '2013-07', '2013-08', '2013-09', '2013-10', '2013-11', '2013-12', '2014-01', '2014-02', '2014-03', '2014-04']

for month in months:
    plot_dow_overlay(month)

