#plot average weekly energy use for certain time range

import os
import pandas as pd
import MySQLdb as sqd
import pandas.io.sql as sql
import matplotlib.pyplot as plt

#set up directory and database connection
os.chdir('/Users/durango/PycharmProjects/Energy Project')
mydb = sqd.connect(host = '127.0.0.1', user = 'root', db = 'rdcep_amanda')

#create dataframe from query
df = sql.read_frame('select * from all_avg_dt where datetime between "2013-04-01" and "2014-04-30"',
                    mydb, parse_dates = ['datetime'], index_col = ['datetime'])

df[['total_energy']] = df[['total_energy']].astype(float)

#average over day of week
df = df.groupby(df.index.dayofweek).mean()
df.index = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

#make the plot
plot = df.plot(figsize = (12,8), legend = False)
plot.margins(0,.1)
plot.set_xlabel('Day of Week', fontsize = 14)
plot.set_ylabel('Energy Consumption in kW/h', fontsize = 14)
plot.set_title('Time vs. Energy Consumption, Week', fontsize = 18)
plt.savefig('/Users/durango/Desktop/RDCEP_Energy/avg_week',dpi=100)

