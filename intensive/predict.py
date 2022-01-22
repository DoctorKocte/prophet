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
start_date = date(2021, 10, 9) 
a = datetime.datetime(2021, 10, 9, 0, 0, 0)
b = datetime.datetime(2022, 2, 28, 0, 0, 0)

#start_date = date(2022, 3, 1) 
#a = datetime.datetime(2022, 3, 1, 0, 0, 0)
#b = datetime.datetime(2022, 6, 29, 0, 0, 0)

delta = (b - a)
minutes = 0

#PATH = "D:/1PROPHET/allinfoMain.csv"
PATH = "D:/1PROPHET/intensity_train.csv"
PATH_TO_CSV = "D:/1PROPHET/allinfoPredict.csv"

#path = "D:/1PROPHET/data.csv"
df = read_csv(PATH, delimiter = ";", header=0)
# prepare expected column names
df['ds'] = to_datetime(df['ds']) #если столбец называется не ds
df.columns = ['ds', 'y']

# define the model
model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
model.fit(df)

future = list()
for index, row in df.iterrows():
    if ((str)(row['ds']) >= (str)(a) and (str)(row['ds']) <= (str)(b)) :
        future.append(row['ds'])


#for k in range(delta.days + 1):
#    day = (start_date + timedelta(days=k)).strftime(format)
#    for i in range(48):
#        q = (((a) + timedelta(minutes=minutes)).strftime(format))
#        future.append(q)
#        minutes += 30

future = DataFrame(future)
future.columns = ['ds']
future['ds'] = to_datetime(future['ds'])

# use the model to make a forecast
forecast = model.predict(future)

#for index, row in future.iterrows():
#    forecast['yhat'] = round(forecast['yhat'])
#    forecast['yhat_upper'] = round(forecast['yhat_upper'])

forecast[['ds', 'yhat']].to_csv(PATH_TO_CSV, sep=';', index=False) 

y_true = list()
for index, row in df.iterrows():
    if ((str)(row['ds']) >= (str)(a) and (str)(row['ds']) <= (str)(b)) :
        y_true.append(row['y'])

y_pred = forecast['yhat'].values

# plot expected vs actual
pyplot.plot(y_true, label='Actual')
pyplot.plot(y_pred, label='Predicted')
pyplot.legend()
pyplot.show()
