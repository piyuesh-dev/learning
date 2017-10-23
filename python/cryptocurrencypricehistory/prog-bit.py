#!/usr/bin/env python3

# Load libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import traceback

#% matplotlib inline

readcols = ['Date', 'Close']
df = pd.read_csv("bitcoin_price.csv", usecols=readcols, parse_dates=['Date'])

# create date index https://stackoverflow.com/questions/35488908/pandas-dataframe-groupby-for-year-month-and-return-with-new-datetimeindex
df = df.set_index('Date')

#print(df.index)

#plt.figure()
f, ax = plt.subplots(2, sharex=True, figsize=(16, 6))

ax[0].plot(df)
ax[0].set_title("Bitcoin historic prices - Daily")
ax[0].set_xlabel("Timeline")
ax[0].set_ylabel("Bitcoin Price in $")

#plt.show()

# resample daily to monthly https://stackoverflow.com/questions/41612641/different-behaviour-with-resample-and-asfreq-in-pandas
df_mon = df.resample('M').mean()

#print(df_mon)

ax[1].plot(df_mon)
ax[1].set_title("Bitcoin Average prices - Monthly")
ax[1].set_xlabel("Timeline")
ax[0].set_ylabel("Bitcoin Price in $")

plt.show()
