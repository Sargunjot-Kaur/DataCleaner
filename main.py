import pandas as pd
from profiler import count_duplicates, missing_vals, whitespace_changes, detect_numeric_columns, count_numeric_issues
from cleaner import strip_whitespace

#reads the csv file into a pandas DataFrame
raw_df = pd.read_csv('customer.csv')
clean_df = raw_df.copy()
clean_df = strip_whitespace(clean_df)

duplicate_count = count_duplicates(clean_df)
missing_values = missing_vals(clean_df)
whitespace_count = whitespace_changes(raw_df, clean_df)


print("Duplicate rows: ", duplicate_count)
print("Missing values per column: ", missing_values)

print("number of whitespaces found: ", whitespace_count)

numeric_columns=detect_numeric_columns(raw_df)
print(numeric_columns)

count_numeric_issues(raw_df, numeric_columns)