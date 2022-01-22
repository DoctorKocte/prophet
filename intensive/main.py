from pandas import read_csv
from pandas import to_datetime
from pandas import DataFrame
from fbprophet import Prophet
from matplotlib import pyplot
import datetime
from datetime import date, timedelta
#from neuralprophet import NeuralProphet

# load data
path = "D:/1PROPHET/intensity_train.csv"        #откуда данные берем
PATH_TO_CSV = "D:/1PROPHET/allinfoMain.csv"     #куда выводим результат

df = read_csv(path, delimiter = ";", header=0)
# prepare expected column names
df['ds'] = to_datetime(df['ds'])
df = df[['ds','y']]
df.columns = ['ds','y']
#df.columns = ['ds', 'y']
# define the model
model = Prophet( yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
model.fit(df)

format = "%Y-%m-%d %H:%M:%S"
start_date = date(2022, 3, 1) 
a = datetime.datetime(2022, 3, 1, 0, 0, 0)
b = datetime.datetime(2022, 6, 29, 0, 0, 0)
delta = (b - a)
minutes = 0

future = list()

#for index, row in df.iterrows():
#    if ((str)(row['ds']) >= (str)(a) and (str)(row['ds']) <= (str)(b)) :
#        future.append(row['ds'])


for k in range(delta.days + 1):
    day = (start_date + timedelta(days=k)).strftime(format)
    for i in range(1):
        q = (((a) + timedelta(minutes=minutes)).strftime(format))
        future.append(q)
        minutes += 1440     #1440 - сутки для тестов

        
future = DataFrame(future)

#df_future = model.make_future_dataframe(df, periods=142, n_historic_predictions=len(df))
#forecast = model.predict(df_future)
future.columns = ['ds']

future['ds'] = to_datetime(future['ds'])
#future = future[['ds','y']]


# use the model to make a forecast
forecast = model.predict(future)

#for index, row in future.iterrows():
#    forecast['yhat'] = round(forecast['yhat'])
#    forecast['yhat_upper'] = round(forecast['yhat_upper'])
    
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(PATH_TO_CSV, sep=';', index=False) 

# plot forecast
model.plot(forecast)
#pyplot.plot(forecast[['yhat_upper']])
pyplot.show()
