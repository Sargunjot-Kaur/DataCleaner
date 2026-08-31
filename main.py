import pandas as pd

#reads the csv file into a pandas DataFrame
raw_df = pd.read_csv('customer.csv')
clean_df = raw_df.copy()

