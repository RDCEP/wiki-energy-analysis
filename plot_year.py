# -*- coding: utf-8 -*-
#plot average energy usage over entire year

import os
import pandas as pd
import MySQLdb as sqd
import pandas.io.sql as sql
import matplotlib.pyplot as plt

#set up directory and database connection
os.chdir('/Users/durango/PycharmProjects/Energy Project')
mydb = sqd.connect(host = '127.0.0.1', user = 'root', db = 'rdcep_amanda')

#create dataframe of energy use over entire year from query
df = sql.read_frame('select * from all_avg_dt', mydb, parse_dates = ['datetime'], index_col = ['datetime'])

df[['total_energy']] = df[['total_energy']].astype(float)

#change index intervals to one day
df_rough = df.resample('1d', how = 'mean')

#make plot
plot = df_rough.plot(figsize = (12,8), legend = False)
plot.set_title('Time vs. Energy Consumption, Year', fontsize = 18)
plot.set_ylabel('Energy Consumption in kW/h', fontsize = 14)
plot.set_xlabel('Time', fontsize = 14)
plt.savefig('/Users/durango/Desktop/RDCEP_Energy/year_rough',dpi=100)


#smoothed out version (change index intervals to one month)
df_smooth = df.resample('1m', how = 'sum')

plot = df_smooth.plot(figsize = (12,8), legend = False)
plot.set_title('Time vs. Energy Consumption, Year', fontsize = 18)
plot.set_ylabel('Energy Consumption in kW/h', fontsize = 14)
plot.set_xlabel('Time', fontsize = 14)
plt.savefig('/Users/durango/Desktop/RDCEP_Energy/year_smooth',dpi=100)
