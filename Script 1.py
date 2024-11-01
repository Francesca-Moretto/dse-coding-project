pyhton script.py
python
print('Hello!')

#library 
import pandas as pd

df_cities = pd.read_csv("worldcitiespop.csv")

print(df_cities)

#analyse the structure of the dataset
print(df_cities.columns)
print(df_cities.head)
print(df_cities.describe)



#check the number of columns in each row
row_column_counts = raw_df.apply(lambda row: len(row.dropna()), axis=1)

#find rows with different number of columns 
inconsistent_rows = raw_df[row_column_counts != row_column_counts.mode()[0]]

