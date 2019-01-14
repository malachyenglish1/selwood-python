#import relevant packages

import numpy as np
import glob
import os

#find most recent folder from directory
list_of_folders = glob.glob('Z:/QuantifiReport/*')
#print(list_of_folders)
latest_folder = max(list_of_folders, key=os.path.getctime)
print(latest_folder)

#import the relevant csv using context manager
trade_file = str(latest_folder) + "\\" + 'LCS_DetailedReport.csv'
print(trade_file)

'''
with open(trade_file, 'r') as file:
    head = [next(trade_file) for x in range (10)]
    print(head)
'''
