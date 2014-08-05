# -*- coding: utf-8 -*-
#write csv with averages across homegroup and changes utctime to Central Time

import os
import MySQLdb as sqd
import pandas.io.sql as sql
import pandas as pd

os.chdir('/Users/durango/PycharmProjects/Energy Project/')
mydb = sqd.connect(host = '127.0.0.1', user = 'root', db = 'rdcep_amanda')
cur = mydb.cursor()

df = sql.read_frame('select utctime, total_energy from readings', mydb, parse_dates = ['utctime'], index_col = 'utctime', coerce_float = True)
df[['total_energy']] = df[['total_energy']].astype(float)

df_all_avg = df.resample('15T', how='mean')

df_all_avg = df_all_avg.tz_localize('UTC').tz_convert('US/Central')

df_all_avg.index = pd.DatetimeIndex([i.replace(tzinfo=None) for i in df_all_avg.index])

df_all_avg.index.name = 'datetime'

df_all_avg.to_csv('all_avg_dt.csv')



