#define function that makes stacked area plot to show how energy use by appliance or room changes over the course of a month
#specify appliances or rooms in "sources" list
#can be for one house_id or averaged acrossed all houses

import os
import pandas as pd
import MySQLdb as sqd
import pandas.io.sql as sql
import matplotlib.pyplot as plt

#set up databse connection
os.chdir('/Users/durango/PycharmProjects/Energy Project')
mydb = sqd.connect(host = '127.0.0.1', user = 'root', db = 'rdcep_amanda')


#make dataframe for one source appliance/room, over the course of one day, averaged over the month, house_id optional
def make_df(source, month, house_id):
    if house_id == 'none':
        #query for data
        df = sql.read_frame('select datetime, '+source+' from grouped_columns where '+source+' > 0 '
                        'and datetime between "'+month+'-01 00:00:00" and "'+month+'-31 23:45:00"',
                        mydb, parse_dates = ['datetime'], index_col = 'datetime')
                        
    else:
        df = sql.read_frame('select datetime, '+source+' from grouped_columns where house_id= "
        '+house_id+'" and '+source+' > 0 and datetime between "'+month+'-01 00:00:00" and "'+month+'
        -30 23:45:00"',mydb, parse_dates = ['datetime'], index_col = 'datetime')
   
    #get daily average in 1h intervals
    df = df.resample('1h', how='mean')
    df.index = df.index.time
    df = df.groupby(df.index).mean()
    df.index = range(0,24)
    return df

#combine and plot
def plot_area(month, house_id):

    #write empty dataframe with time index
    df = pd.DataFrame(index= range(0,24))
    
    #adjust sources to those to be analyzed
    sources = ['lights_plugs', 'furnace', 'refrigerator',  'waterheater', 'subpanel', 'drye', 'air', 'pool']
    #sources = ['bedroom','garage','office','kitchen','utilityroom','livingroom', 'diningroom', 'bathroom']
    
    #compile the individual source dataframes
    for source in sources:
        df = df.join(make_df(source, month, house_id))
    
    my_colors = ([.4,1,0],[.059,.439,0],[1,0,0],[.09,.706,.694],[.686,0,.698],[.698,.706,.027],[0,0,0],[0,0,1])
    #my_colors = ([.059,.439,0],[1,0,0],[.09,.706,.694],[0,0,0],[.698,.706,.027])
    
    #make the plot
    plot = df.plot(kind='area', stacked=True, figsize = (12,8), color=my_colors, legend = False)
    
    plot.set_ylabel('Energy Consumption in kW/h', fontsize = 14)
    plot.set_xlabel('Hour of Day', fontsize = 14)
    
    if house_id == 'none':
        plot.set_title('Energy Consumption by Room in ' +month, fontsize = 16)
        plt.savefig('/Users/durango/Desktop/RDCEP_Energy/stacked_area_plots/app_' + month, dpi=100)
    else:
        plot.set_title('Energy Consumption by Room in ' +month+ ' house_id='+house_id, fontsize = 16)
        plt.savefig('/Users/durango/Desktop/RDCEP_Energy/stacked_area_plots/room_' + month + '_' + house_id, dpi=100)
   
plot_area('2013-12', 'none')