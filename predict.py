# make an out-of-sample forecast
from pandas import read_csv
from pandas import to_datetime
from pandas import DataFrame
from fbprophet import Prophet
from matplotlib import pyplot
#import psycopg2
#from sklearn.metrics import mean_absolute_error

# load data
path = "D:/Projects/prophet/data.csv"
df = read_csv(path, header=0)
# prepare expected column names
df.columns = ['ds', 'y']
df['ds'] = to_datetime(df['ds'])

# define the model
model = Prophet()
# fit the model
model.fit(df)

future = list()
a = "2012-12-10"
for index, row in df.iterrows():
    if ((str)(row['ds']) > (str)(a)) :
        future.append(row['ds'])
        
future = DataFrame(future)
future.columns = ['ds']
future['ds'] = to_datetime(future['ds'])
# use the model to make a forecast
forecast = model.predict(future)
# summarize the forecast
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())
# plot forecast
model.plot(forecast)
pyplot.show()
