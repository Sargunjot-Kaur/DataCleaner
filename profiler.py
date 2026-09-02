import pandas as pd

def count_duplicates(df):
    return df.duplicated().sum()

def missing_vals(df):
    return df.isna().sum()

def whitespace_changes(raw_df, clean_df):
    total = 0

    for column in raw_df.columns:
        changes = (raw_df[column] != clean_df[column])
        total += changes
    return total    

numeric_columns = []
def detect_numeric_columns (df):
    for column in df.columns:
        series = df[column]
        converted = pd.to_numeric(series, errors = "coerce")
        
        ratio_numeric = converted.notna().sum() / series.notna().sum()
        
        if ratio_numeric >= 0.8:
                numeric_columns.append(column)

    return numeric_columns        

def count_numeric_issues(df, numeric_columns):
    for column in numeric_columns:
         series = df[column]
         converted = pd.to_numeric(series, errors = "coerce")
         count= (series.notna() & converted.isna()).sum()

         print (column, count)
    
              
    
