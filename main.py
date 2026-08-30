import pandas as pd

#reads the csv file into a pandas DataFrame
df = pd.read_csv('customer.csv')

#number of columns
print(df.shape[1]) 

#names of the columns
print(df.columns)

#number of missing values per column
print(df.isna().sum())

#nube of duplicated rows
print(df.duplicated().sum())