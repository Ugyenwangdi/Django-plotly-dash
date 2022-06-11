import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# df = pd.read_csv('bhutan_fuel_prices.csv') # , parse_dates=['Approved_Date'], index_col='Approved_Date'
# df.head()
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv') 
print(df.head())

# df['Product'] = df['Product'].replace('HSD (in KL)', 'Diesel')
# df['Product'] = df['Product'].replace('MS (in KL)', 'Petrol')
# df.head()


# index_names = df[ df['Region'] == '\x1a' ].index
  
# # drop these row indices from dataFrame
# df.drop(index_names, inplace = True)


# # Drop the "RSP/KL" column
# df.drop(["RSP/KL"], axis = 1, inplace = True)


# # print(df.values.tolist())


