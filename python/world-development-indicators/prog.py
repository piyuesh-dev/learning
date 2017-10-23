#!/usr/bin/env python3

# Load libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import traceback

# method to draw line plots for different india pakistan parameters
def drawLinePlots(ax, key1, key2, parameter='Hospital beds (per 1,000 people)'):

	""" This method is used to display lines plots based on input data """
	tmpdf1 = df_list[key1]
	tmpdf2 = df_list[key2]

	df_key1_data = tmpdf1[tmpdf1['IndicatorName'] == parameter]
	df_key2_data = tmpdf2[tmpdf2['IndicatorName'] == parameter]

	# set name of index columns to Year
	df_key1_data.set_index('Year', inplace=True)
	df_key2_data.set_index('Year', inplace=True)
	
	# set name of Value column to Country name
	df_key1_data.rename(columns={"Value": key1}, inplace= True)
	df_key2_data.rename(columns={"Value": key2}, inplace= True)

	res = pd.concat([df_key1_data.iloc[:,3], df_key2_data.iloc[:,3]], axis=1)

	try:
		# remove NaN values
		res = res.dropna() 
		res.plot(ax=ax, title=parameter)
	except:	
		print("This is an error message!")
		traceback.print_exc()
	

# read indicators csv, filters out India & pakistan data for populations
# mortality rate (male, female) for as many years.

file = 'Indicators.csv'
readcols = ['CountryName', 'CountryCode', 'IndicatorName', 'Year', 'Value']

df_ind = pd.DataFrame()
df_pak = pd.DataFrame()
df_kor = pd.DataFrame()

for chunk in pd.read_csv(file, chunksize=10000, usecols=readcols):
	tmpdf1 = chunk[chunk['CountryCode'] == 'IND']
	tmpdf2 = chunk[chunk['CountryCode'] == 'PAK']
	tmpdf3 = chunk[chunk['CountryCode'] == 'KOR']
	
	if (tmpdf1.empty != True):
		df_ind = df_ind.append(tmpdf1)

	if (tmpdf2.empty != True):
		df_pak = df_pak.append(tmpdf2)
		
	if (tmpdf3.empty != True):
		df_kor = df_kor.append(tmpdf3)

# dict of country wise data frames....
df_list = {"India": df_ind, "Pakistan": df_pak, "Korea": df_kor}

# draw various plots for India & Pakistan
# like hospital beds per 1000 persons

fig, ax = plt.subplots(nrows=2,ncols=3, figsize=(20, 8))

# display various plots on single screen refer https://stackoverflow.com/questions/22483588/how-can-i-plot-separate-pandas-dataframes-as-subplots
drawLinePlots(ax[0][0], "India", "Pakistan", parameter = 'Life expectancy at birth, total (years)')
drawLinePlots(ax[0][1], "India", "Pakistan", parameter = 'Hospital beds (per 1,000 people)')
drawLinePlots(ax[1][2], "India", "Pakistan", parameter = 'CO2 emissions (metric tons per capita)')
drawLinePlots(ax[1][0], "India", "Pakistan", parameter = 'GDP per capita (current US$)')
drawLinePlots(ax[1][1], "India", "Pakistan", parameter = 'GDP at market prices (current US$)')
drawLinePlots(ax[0][2], "India", "Pakistan", parameter = 'Exports of goods and services (current US$)')

plt.show()

plt.gcf().clear()
fig, ax1 = plt.subplots(nrows=2,ncols=3, figsize=(20, 8))
# draw same plots for India & Korea
# display various plots on single screen refer https://stackoverflow.com/questions/22483588/how-can-i-plot-separate-pandas-dataframes-as-subplots
drawLinePlots(ax1[0][0], "India", "Korea", parameter = 'Life expectancy at birth, total (years)')
drawLinePlots(ax1[0][1], "India", "Korea",  parameter = 'Hospital beds (per 1,000 people)')
drawLinePlots(ax1[1][2], "India", "Korea",  parameter = 'CO2 emissions (metric tons per capita)')
drawLinePlots(ax1[1][0], "India", "Korea",  parameter = 'GDP per capita (current US$)')
drawLinePlots(ax1[1][1], "India", "Korea",  parameter = 'GDP at market prices (current US$)')
drawLinePlots(ax1[0][2], "India", "Korea",  parameter = 'Exports of goods and services (current US$)')

plt.show()

exit()