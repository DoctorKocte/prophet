# make an out-of-sample forecast
from pandas import read_csv
from pandas import to_datetime
from pandas import DataFrame
from fbprophet import Prophet
from matplotlib import pyplot
#import psycopg2
from sklearn.metrics import mean_absolute_error

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
# calculate MAE between expected and predicted values for december
y_true = df['y'].values #рассчитываем ошибку на данных за 12 месяцев
y_pred = forecast['yhat'].values
mae = mean_absolute_error(y_true, y_pred)
print('MAE: %.3f' % mae)
# plot expected vs actual
pyplot.plot(y_true, label='Actual')
pyplot.plot(y_pred, label='Predicted')
pyplot.legend()
pyplot.show()
