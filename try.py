# make an out-of-sample forecast
from pandas import read_csv
from pandas import to_datetime
from pandas import DataFrame
from fbprophet import Prophet
from matplotlib import pyplot
import csv
#import psycopg2


# load data
a = "2020-10-18"
b = "2020-10-20"

path = "D:/Projects/prophet/ForProph.csv"
df = read_csv(path, delimiter = ";", header=0)
# prepare expected column names
df.columns = ['ds', 'y']
df['ds'] = to_datetime(df['ds'])

# define the model
model = Prophet()
# fit the model
model.fit(df)

future = list()

for index, row in df.iterrows():
    if ((str)(row['ds']) >= (str)(a) and (str)(row['ds']) <= (str)(b)) :
        future.append(row['ds'])
        
future = DataFrame(future)
future.columns = ['ds']
future['ds'] = to_datetime(future['ds'])
# use the model to make a forecast
forecast = model.predict(future)

forecast[['ds', 'yhat', 'yhat_upper']].to_csv('D:/Projects/prophet/allinfo.csv',index=False) 

y_true = list()
for index, row in df.iterrows():
    if ((str)(row['ds']) >= (str)(a) and (str)(row['ds']) <= (str)(b)) :
        y_true.append(row['y'])

y_pred = forecast['yhat_upper'].values

# plot expected vs actual
pyplot.plot(y_true, label='Actual')
pyplot.plot(y_pred, label='Predicted')
pyplot.legend()
pyplot.show()
