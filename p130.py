import pandas as pd
import csv
df=pd.read_csv("bright_stars.csv")
del df ["Luminosity"]
print(list(df))
df.to_csv('main.csv') 