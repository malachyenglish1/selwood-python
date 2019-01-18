# import relevant packages
import numpy as np
import pandas as pd
import glob
import os
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta, FR

#user-defined module to find the relevant days
import findlastdays as flday

# some display options for the terminal relevant to pandas
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

#The dates are now in datetime.date format
print("Yesterday is: ", date.today() - timedelta(1))
print("The most recent weekday is: ", flday.prev_weekday(date.today()))
print("The most recent Friday is: ", flday.prev_friday(date.today()))

# create a dictionary of days - key: relative day, value: the date
key_dates = {"Yesterday": date.today() - timedelta(1)
             ,"Last Day": flday.prev_weekday(date.today())
             ,"Last Friday": flday.prev_friday(date.today())}
print(key_dates)

# note the conversion to string and format to be able to seek the file
detail_file = 'Z:/QuantifiReport/' + key_dates["Last Day"].strftime('%Y%m%d') + "\\" + 'LCS_DetailedReport.csv'
print(detail_file)

trade_file = 'Z:/QuantifiReport/' + key_dates["Last Day"].strftime('%Y%m%d') + "\\" + 'LCS_TradeReport.csv'
print(trade_file)

# check the first five lines of the file and the header
# use pandas to import the csv as a dataframe within a context manager
# parsing the Trade Date column is needed
# using dayfirst= True ensures correct upload of dates with parsing
with open(trade_file, 'r') as f:
    df = pd.read_csv(f,  parse_dates = ['Trade Date'], dayfirst=True)
    df = df[['TradeId',
            'Trade Date',
            'Maturity',
            'Counterparty',
            'Description',
            'Notional',
            'InitialMargin',
            'Attach',
            'Detach',
            
            ]]
#print(list(df.columns.values))
print(df.head())

# remove duplicate TradeId's
df = df.drop_duplicates(subset=["TradeId"], keep= 'first')
print("Total number of trades: " + str(len(df.index)))
df.set_index("TradeId", inplace = True)

print(key_dates["Last Friday"])
print(type(key_dates["Last Friday"]))


## Make sure both the column and the date match data formats:
# converts date to datetime64
key_dates["Last Friday"] = np.datetime64(key_dates["Last Friday"])

# converts column to datetime64[ns]
#df['Trade Date'] = pd.to_datetime(df['Trade Date'])

df_fri = df.loc[df['Trade Date'] > key_dates["Last Friday"]]
df_last = df.loc[df['Trade Date'] == df['Trade Date'].max()]

print(df_fri.shape)
print(df_last.shape)
print(df_fri.head())
print(df_last.head())

#N.b. the file needs to be closed to overwrite.
#Error handle this with user input
df_fri.to_csv('Z:/Malachy/python/projects/fri_trades.csv')
#df_fri[df_fri['Notional'] > 0].to_html('Z:/Malachy/python/projects/fri_trades_longrisk.html')
#df_fri[df_fri['Notional'] < 0].to_html('Z:/Malachy/python/projects/fri_trades_shortrisk.html')

df_last.to_csv('Z:/Malachy/python/projects/new_trades.csv')
df_last[df_last['Notional'] > 0].to_html('Z:/Malachy/python/projects/new_trades_longrisk.html')
df_last[df_last['Notional'] < 0].to_html('Z:/Malachy/python/projects/new_trades_shortrisk.html')
