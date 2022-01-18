import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
from fbprophet import Prophet


# Load test data: log-transformed daily page views for the Wikipedia page for Peyton Manning.
df = pd.read_csv("D:/Projects/prophet/data.csv")
a = date(2013, 12, 10)
if ((str)(df['ds']) > "2012-12-10") :
    print("aaa")
else: print("sss")

future = list()
a = "2012-12-10"
for index, row in df.iterrows():
    if ((str)(row['ds']) > (str)(a)) :
        future.append(row['ds'])

print(future)


