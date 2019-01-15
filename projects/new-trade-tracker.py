#import relevant packages

import numpy as np
import pandas as pd
import glob
import os

#Some display options for the terminal relevant to pandas
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

from datetime import datetime
from dateutil.relativedelta import relativedelta, FR

#This gives the last Fri before today
#Can use this to pull the most relevant report and to check the differences in trades
datetime.now() + relativedelta(weekday=FR(-1))

#find most recent folder from directory
list_of_folders = glob.glob('Z:/QuantifiReport/*')
#print(list_of_folders)
latest_folder = max(list_of_folders, key=os.path.getctime)
print(latest_folder)

#import the relevant csv using context manager
datail_file = str(latest_folder) + "\\" + 'LCS_DetailedReport.csv'
print(datail_file)

trade_file = str(latest_folder) + "\\" + 'LCS_TradeReport.csv'
print(trade_file)

#Check the first five lines of the file and the header
#Use pandas to import the csv as a dataframe within a context manager
with open(datail_file, 'r') as f:
    df = pd.read_csv(f)
    print(df.head())
    print(list(df.columns.values))
    #remove duplicate TradeId's
    df = df.drop_duplicates(subset=["TradeId"], keep= 'first')
    df.set_index("TradeId", inplace = True)
    print(df.loc[:, ["Description"]].head())
    print("Total number of trades: " + str(len(df.index)))
    print(df.shape)


'''
#Check the top 3 lines of the file
with open(trade_file, 'r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    head = [next(file) for x in range (3)]
    print(head)
'''

#
