from pandas import read_csv
from pandas import to_datetime
from pandas import DataFrame
from fbprophet import Prophet
from matplotlib import pyplot
import csv
import datetime
from datetime import timedelta
from datetime import date, timedelta


# диапазон 

format = "%Y-%m-%d %H:%M:%S"
#start_date = date(2021, 10, 9) 
#a = datetime.datetime(2021, 10, 9, 0, 0, 0)
#b = datetime.datetime(2022, 2, 28, 0, 0, 0)

start_date = date(2022, 3, 1) 
a = datetime.datetime(2022, 3, 1, 0, 0, 0)
b = datetime.datetime(2022, 6, 29, 0, 0, 0)

#start_date = date(2021, 10, 10) 
#a = datetime.datetime(2021, 10, 10, 0, 0, 0)
#b = datetime.datetime(2022, 2, 25, 0, 0, 0)

delta = (b - a)
minutes = 0

PATH = "D:/1PROPHET/allinfoMain.csv"
PATH_TO_FILE = "D:/1PROPHET/intensity_test.csv"

df = read_csv(PATH, delimiter = ";", header=0)
# prepare expected column names
df['ds'] = to_datetime(df['ds']) #если столбец называется не ds
df.columns = ['ds', 'y']

frcst = read_csv(PATH_TO_FILE, delimiter = ";", header=0)
frcst['ds'] = to_datetime(frcst['ds']) #если столбец называется не ds
frcst.columns = ['ds', 'y']

y_true = list()
for index, row in df.iterrows():
    if ((str)(row['ds']) >= (str)(a) and (str)(row['ds']) <= (str)(b)) :
        y_true.append(row['y'])

#y_pred = frcst['y'].values

y_pred = list()
for index, row in frcst.iterrows():
    if ((str)(row['ds']) >= (str)(a) and (str)(row['ds']) <= (str)(b)) :
        y_pred.append(row['y'])

# plot expected vs actual
pyplot.plot(y_pred, label='Actual')
pyplot.plot(y_true, label='Predicted')
pyplot.legend()
pyplot.show()
