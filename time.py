from pandas import read_csv
from pandas import to_datetime
from random import randint as rand

df = read_csv("D:/Projects/prophet/alldates.csv", sep=(';'))
res = df[['Origin', 'Destination', 'Speed']]
 
dt = list()
for idx1 in range(len(df)):
    temp = '%s %02d:%02d:%02d' % (df['DATE'][idx1], df['HOUR'][idx1], rand(0, 59), rand(0, 59))
    dt.append(temp)
 
# print(dt)
res['TimeRequest'] = dt
 
res['TimeRequest'] = to_datetime(res['TimeRequest'])
print(res)

res[['Origin', 'Destination', 'TimeRequest']].to_csv('D:/Projects/prophet/alldatesinfo.csv',index=False) 

# print(dt)
