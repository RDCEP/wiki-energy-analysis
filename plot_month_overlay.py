#plot energy use for each month on one plot

import os
import pandas as pd
import MySQLdb as sqd
import pandas.io.sql as sql
import matplotlib.pyplot as plt

#set up database connection
os.chdir('/Users/durango/PycharmProjects/Energy Project')
mydb = sqd.connect(host = '127.0.0.1', user = 'root', db = 'rdcep_amanda')

#create dataframe with average energy use against time
df = sql.read_frame('select * from all_avg_dt', mydb, parse_dates = ['datetime'], index_col = ['datetime'])

#convert data values to floats
df[['total_energy']] = df[['total_energy']].astype(float)

#create month, day MultiIndex
df.index = pd.MultiIndex.from_arrays([df.index.month, df.index.day], names=['month','day'])

#sum up 15 minute intervals to get daily total
df = df.groupby(level=(0,1), axis=0).sum()

#pivot table so months are on x-axis
df = df.unstack(level = -2)
df.columns = df.columns.droplevel(level=0)
df.columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#make the plot
plot = df.plot(figsize = (12,8), colors = ([0,0,1],[0,.5,1],[0,1,1],[0,1,0],[.6,1,0],[.8,1,0],[1,.5,0],[1,0,0],[1,0,.6],[1,0,1],[.6,0,1],[0,.3,1]))
plot.set_xlabel('Day', fontsize = 14)
plot.set_ylabel('Energy Consumption in kW/h', fontsize = 14)
plot.set_title('Energy Consumption by Month', fontsize = 18)
plot.legend(bbox_to_anchor = (1.1, 1), shadow = True, fontsize = 14)
plt.savefig('/Users/durango/Desktop/RDCEP_Energy/month_overlay', dpi=100)


