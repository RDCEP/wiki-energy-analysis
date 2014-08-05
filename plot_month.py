#plot simple line graph of energy use over one month

import os
import pandas as pd
import matplotlib.pyplot as plt

#set up directory
os.chdir('/Users/durango/PycharmProjects/Energy Project')

#function that splits dataframe index into year, month, and day
def split(df):
    df = df.copy()
    df['year'] = pd.DatetimeIndex(df.index).year
    df['month'] = pd.DatetimeIndex(df.index).month
    df['day'] = pd.DatetimeIndex(df.index).day
    return df

#for all months except April because April has data for 2013 AND 2014
def plot_month(month_no, month_name):

    #make dataframe from csv
    df = pd.read_csv('Home Group A (averaged)/2014-' + month_no + '_avg.csv', parse_dates=True, index_col='time')
    
    #get total energy use per day instead of 15min intervals
    df.index = pd.MultiIndex.from_arrays([df.index.date, df.index.time], names=['date','time'])
    df = df.sum(level=0)
    df.columns=['use_sum']

    #make dataframe of use_sum with day index
    df = split(df)
    df = df.set_index(['day'])
    df=pd.DataFrame(df['use_sum'])

    #make the plot
    plot = df.plot(figsize = (12,8), title = month_name + ' 2014', legend = False)
    plot.set_ylabel('Energy Consumption in kW/h')
    plt.savefig('/Users/durango/Desktop/RDCEP_Energy/time_use_linegraphs_by_month/'+ month_name, dpi=100)


plot_month('03', 'March')





# plot April (2013,2014)

df2013 = pd.read_csv('Home Group A (averaged)/2013-04_avg.csv', parse_dates=True, index_col='time')
df2013.index = pd.MultiIndex.from_arrays([df2013.index.date, df2013.index.time], names=['date','time'])
df2013 = df2013.sum(level=0)
df2013.columns=['use_sum']

df2014 = pd.read_csv('Home Group A (averaged)/2014-04_avg.csv', parse_dates=True, index_col='time')
df2014.index = pd.MultiIndex.from_arrays([df2014.index.date, df2014.index.time], names=['date','time'])
df2014 = df2014.sum(level=0)
df2014.columns=['use_sum']

df2013 = split(df2013)
df2014 = split(df2014)

df2013.rename(columns={'use_sum':'use_sum_2013-04'}, inplace=True)
df2014.rename(columns={'use_sum':'use_sum_2014-04'}, inplace=True)

df2013 = df2013.set_index(['day'])
df2014 = df2014.set_index(['day'])

df2013=pd.DataFrame(df2013['use_sum_2013-04'])
df2014=pd.DataFrame(df2014['use_sum_2014-04'])

joined = df2013.join(df2014)

plot = joined.plot(figsize = (12,8), title = 'April 2013-2014')
plot.set_ylabel('Energy Consumption in kW/h')
plt.savefig('/Users/durango/Desktop/RDCEP_Energy/time_use_linegraphs_by_month/april', dpi=100)