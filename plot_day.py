# -*- coding: utf-8 -*-
#plot average weekday, average Saturday, and average Sunday on same plot

import os
import pandas as pd
import MySQLdb as sqd
import pandas.io.sql as sql
import matplotlib.pyplot as plt

#set up database connection
os.chdir('/Users/durango/PycharmProjects/Energy Project')
mydb = sqd.connect(host = '127.0.0.1', user = 'root', db = 'rdcep_amanda')

#create dataframes for each day of week
df_sunday = sql.read_frame('select * from all_avg_dt where dayname(datetime) = "Sunday" and datetime between "2013-04-01" and "2014-04-30"',
                    mydb, parse_dates = ['datetime'], index_col = ['datetime'])
df_monday = sql.read_frame('select * from all_avg_dt where dayname(datetime) = "Monday" and datetime between "2013-04-01" and "2014-04-30"',
                    mydb, parse_dates = ['datetime'], index_col = ['datetime'])
df_tuesday = sql.read_frame('select * from all_avg_dt where dayname(datetime) = "Tuesday" and datetime between "2013-04-01" and "2014-04-30"',
                    mydb, parse_dates = ['datetime'], index_col = ['datetime'])
df_wednesday = sql.read_frame('select * from all_avg_dt where dayname(datetime) = "Wednesday" and datetime between "2013-04-01" and "2014-04-30"',
                    mydb, parse_dates = ['datetime'], index_col = ['datetime'])
df_thursday = sql.read_frame('select * from all_avg_dt where dayname(datetime) = "Thursday" and datetime between "2013-04-01" and "2014-04-30"',
                    mydb, parse_dates = ['datetime'], index_col = ['datetime'])
df_friday = sql.read_frame('select * from all_avg_dt where dayname(datetime) = "Friday" and datetime between "2013-04-01" and "2014-04-30"',
                    mydb, parse_dates = ['datetime'], index_col = ['datetime'])
df_saturday = sql.read_frame('select * from all_avg_dt where dayname(datetime) = "Saturday" and datetime between "2013-04-01" and "2014-04-30"',
                    mydb, parse_dates = ['datetime'], index_col = ['datetime'])

#convert values to floats
df_sunday[['total_energy']] = df_sunday[['total_energy']].astype(float)
df_monday[['total_energy']] = df_monday[['total_energy']].astype(float)
df_tuesday[['total_energy']] = df_tuesday[['total_energy']].astype(float)
df_wednesday[['total_energy']] = df_wednesday[['total_energy']].astype(float)
df_thursday[['total_energy']] = df_thursday[['total_energy']].astype(float)
df_friday[['total_energy']] = df_friday[['total_energy']].astype(float)
df_saturday[['total_energy']] = df_saturday[['total_energy']].astype(float)

#create weekday dataframe
df_weekday = df_monday.append(df_tuesday.append(df_wednesday.append(df_thursday.append(df_friday))))

#get the average for each 15min interval
df_weekday = df_weekday.groupby(df_weekday.index.time).mean()
df_sunday = df_sunday.groupby(df_sunday.index.time).mean()
df_saturday = df_saturday.groupby(df_saturday.index.time).mean()

#rename columns to reflect what they show
df_weekday.columns = ['weekday']
df_saturday.columns = ['Saturday']
df_sunday.columns = ['Sunday']

#join the dataframes into one dataframe
df = df_weekday.join([df_saturday, df_sunday])

#make the plot
plot = df.plot(figsize = (12,8))
plot.set_title('Time vs. Avg Daily Energy Consumption', fontsize = 18)
plot.set_ylabel('Energy Consumption in kW/h', fontsize = 14)
plot.set_xlabel('time', fontsize = 14)
plot.legend(shadow = True, fontsize = 14)
plt.savefig('/Users/durango/Desktop/RDCEP_Energy/TUE in April',dpi=100)


