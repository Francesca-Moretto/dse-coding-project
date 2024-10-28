pyhton script.py
python
print('Hello!')

#library 
import pandas as pd

#import file csv
cities_df = pd.read_csv('C:/Users/39348/Documents/Università/Magistrale/In corso/Coding/worldcitiespop.csv')

#analyse the structure of the dataset
print(cities_df.head)
print(cities_df.columns)

#fixing the first row with the names of columns 
cities_df = pd.read_csv('C:/Users/39348/Documents/Università/Magistrale/In corso/Coding/worldcitiespop.csv', header=None)
print(cities_df.head())
cities_df.columns = ['Country', 'City', 'AccentCity', 'Region', 'Population', 'Latitude', 'Longitude']
print(cities_df.head) #still not good format 

#import keeping row structure
raw_df = pd.read_csv('C:/Users/39348/Documents/Università/Magistrale/In corso/Coding/worldcitiespop.csv', header=None)

#check the number of columns in each row
row_column_counts = raw_df.apply(lambda row: len(row.dropna()), axis=1)

#find rows with different number of columns 
inconsistent_rows = raw_df[row_column_counts != row_column_counts.mode()[0]]