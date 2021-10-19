import pandas as pd 
import csv 

df = pd.read_csv("bright_stars.csv")
del df["Luminosity"]
df.to_csv("main.csv")
df = pd.read_csv('bright_stars.csv')
df
df.columns
final_data = df.dropna()
final_data
final_data.reset_index(drop=True,inplace = True)
final_data
final_data.to_csv('final_data.csv')
final_data.describe()
final_data.head(5)
final_data.dtypes
print(df.shape)
print(list(df))
