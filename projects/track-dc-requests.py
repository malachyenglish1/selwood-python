# import relevant packages
import numpy as np
import pandas as pd
import glob
import os
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta, FR


# some display options for the terminal relevant to pandas
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

# gets most recent prior weekday
def prev_weekday(adate):
    adate -= timedelta(days=1)
    while adate.weekday() > 4: # Mon-Fri are 0-4
        adate -= timedelta(days=1)
    adate -= timedelta(days=1)
    return adate

print(prev_weekday(date.today()))
print(type(prev_weekday(date.today())))

# gets most recent prior Friday
def prev_friday(adate):
    adate -= timedelta(days=1)
    while adate.weekday() != 4: # Fri is 4
        adate -= timedelta(days=1)
    return adate

# create a dictionary of days - key: relative day, value: the date
key_dates = {"Last Day": prev_weekday(date.today())
             ,"Last Friday": prev_friday(date.today())}
print(key_dates)

# note the conversion to string and format to be able to seek the file
print("The latest report is dated: ", key_dates["Last Day"].strftime('%Y%m%d'))
print("Last Friday's report is dated: ", key_dates["Last Friday"].strftime('%Y%m%d'))

detail_file = 'Z:/QuantifiReport/' + key_dates["Last Day"].strftime('%Y%m%d') + "\\" + 'LCS_DetailedReport.csv'
print(detail_file)

trade_file = 'Z:/QuantifiReport/' + key_dates["Last Day"].strftime('%Y%m%d') + "\\" + 'LCS_TradeReport.csv'
print(trade_file)

# check the first five lines of the file and the header
# use pandas to import the csv as a dataframe within a context manager
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


df2 = df.loc[df['Trade Date'] > key_dates["Last Friday"]]

print(df2.shape)
print(df2.head())

#N.b. the file needs to be closed to overwrite.
#Error handle this with user input
df2.to_csv('Z:/Malachy/python/projects/new_trades.csv')
df2[df2['Notional'] > 0].to_html('Z:/Malachy/python/projects/new_trades_longrisk.html')
df2[df2['Notional'] < 0].to_html('Z:/Malachy/python/projects/new_trades_shortrisk.html')
