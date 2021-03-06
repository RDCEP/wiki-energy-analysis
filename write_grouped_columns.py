# -*- coding: utf-8 -*-
#write csv that groups together similar columns

import os
import pandas as pd
import MySQLdb as sqd
import pandas.io.sql as sql


#set up directory and database connection
os.chdir('/Users/durango/PycharmProjects/Energy Project')
mydb = sqd.connect(host = '127.0.0.1', user = 'root', db = 'rdcep_amanda')

#create empty dataframe
df_grouped = pd.DataFrame()

#write new grouped columns
df_grouped['house_id'] = df['house_id']
df_grouped['total_energy'] = df['total_energy']
df_grouped['air'] = df['air1'] + df['air2'] + df['air3']
df_grouped['aquarium'] = df['aquarium1']
df_grouped['bathroom'] = df['bathroom1'] + df['bathroom2']
df_grouped['bedroom'] = df['bedroom1'] + df['bedroom2'] + df['bedroom3'] + df['bedroom4'] + df['bedroom5']
df_grouped['clotheswasher'] = df['clotheswasher1']
df_grouped['clotheswasher_dryg'] = df['clotheswasher_dryg1']
df_grouped['diningroom'] = df['diningroom1'] + df['diningroom2']
df_grouped['dishwasher'] = df['dishwasher1']
df_grouped['drye'] = df['drye1']
df_grouped['dryg'] = df['dryg1']
df_grouped['freezer'] = df['freezer1']
df_grouped['furnace'] = df['furnace1'] + df['furnace2']
df_grouped['garage'] = df['garage1'] + df['garage2']
df_grouped['heater'] = df['heater1']
df_grouped['housefan'] = df['housefan1']
df_grouped['icemaker'] = df['icemaker1']
df_grouped['jacuzzi'] = df['jacuzzi1']
df_grouped['kitchen'] = df['kitchen1'] + df['kitchen2']
df_grouped['kitchenapp'] = df['kitchenapp1'] + df['kitchenapp2']
df_grouped['lights_plugs'] = df['lights_plugs1'] + df['lights_plugs2'] + df['lights_plugs3'] + df['lights_plugs4'] + df['lights_plugs5'] + df['lights_plugs6']
df_grouped['livingroom'] = df['livingroom1'] + df['livingroom2']
df_grouped['microwave'] = df['microwave1']
df_grouped['office'] = df['office1']
df_grouped['outsidelights_plugs'] = df['outsidelights_plugs1'] + df['outsidelights_plugs2']
df_grouped['oven'] = df['oven1'] + df['oven2']
df_grouped['pool'] = df['pool1'] + df['pool2'] + df['poollight1'] + df['poolpump1']
df_grouped['pump'] = df['pump1']
df_grouped['range'] = df['range1']
df_grouped['refrigerator'] = df['refrigerator1'] + df['refrigerator2']
df_grouped['subpanel'] = df['subpanel1'] + df['subpanel2']
df_grouped['utilityroom'] = df['utilityroom1']
df_grouped['unknown'] = df['unknown1'] + df['unknown2'] + df['unknown3'] + df['unknown4']
df_grouped['waterheater'] = df['waterheater1'] + df['waterheater2']
df_grouped['winecooler'] = df['winecooler1']

#write dataframe to csv
df_grouped.to_csv('grouped_columns.csv')

