# Find list of all of the current bespokes
# Take data from Quantifi report csv's
# Remove duplicates
# Create list of unique ticker-portfolio pairs


import pandas as pd

filename = str('Z:/QuantifiReport/20190107/LCS_DetailedReport.csv')
with open (filename, 'r') as file:
    data = pd.read_csv(filename)
    data.head

file_name = str('Z:/QuantifiReport/20190107/LCS_TradeReport.csv')
with open (file_name, 'r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())


