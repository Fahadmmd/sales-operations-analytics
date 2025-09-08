import pandas as pd

df = pd.read_csv("sales.csv")
df.info()   # check columns
df.drop_duplicates(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
df.dropna(inplace=True)
df.to_csv("cleaned_sales.csv", index=False)
print(df.info())  # verify changes