def strip_value (value):
    if isinstance (value, str):
        return value.strip()
    else:
        return value

def strip_whitespace (df):
    for column in df.columns:
        df[column] = df[column].map(strip_value)
    return df


    