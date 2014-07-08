import pandas as pd
import os
import re

def df_for_all_houses(year, month):
	"""month: number"""
	dir_name = 'A-{0}-{1:02d}'.format(year, month)
	dir_path = 'Home Group A/{0}'.format(dir_name)
	use_series = {}
	for entry in os.listdir(dir_path):
		file_path = '{0}/{1}'.format(dir_path, entry)
		match = re.match('DATA_(\d+).csv', entry)
		if not match:
			continue
		print file_path
		house_id = int(match.group(1))
		df = pd.read_csv(file_path, index_col='utc', parse_dates=True)
		index = df.index
		use_series['use_{0}'.format(house_id)] = df.use
	return pd.DataFrame(data=use_series, index=index)

def mean_by_timeslice(df):
	return df.T.mean()

pairs = [(2013, m) for m in range(4, 13)] + [(2014, m) for m in range(1, 5)]
pairs.remove((2013, 11))

dfs = {}
for year, month in pairs:
	dfs[(year, month)] = df_for_all_houses(year, month)

# ugh
means = {}
for year, month in dfs:
	means[(year, month)] = mean_by_timeslice(dfs[(year, month)])
