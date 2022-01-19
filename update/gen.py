import datetime
from random import randint as rand
import psycopg2
import csv


class req(object):

    def __init__(self, origin=1, destination=1, SeatNumber=1, TimeRequest=None):
        self.origin = origin  # место отправки
        self.destination = destination  # место назначения
        self.SeatNumber = SeatNumber  # кол-во запрашиваемых мест
        self.TimeRequest = TimeRequest  # время отправки заявки

    def show(self, counter):
        print(f"{counter}.origin={self.origin}"
              f"  destination={self.destination}"
              f"  SeatNumber={self.SeatNumber}"
              f"  TimeRequest={self.TimeRequest}")

    def gen(self):
        self.origin = stations[rand(0, 8)]
        self.destination = stations[rand(self.origin, 9)]
        self.SeatNumber = rand(1, 8)
        self.TimeRequest = datetime.datetime(2021, 10, rand(18, 25), rand(0, 23), rand(0, 59), rand(0, 59))


# в теории будут названия, хотя можно будет просто заменить нумерацией
stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

con = psycopg2.connect(
    database="postgres",
    user="postgres",  # doctor
    password="6675",  # 6675
    host="127.0.0.1",
    port="5432"
)
print("Database opened successfully")

cur = con.cursor()
if __name__ == '__main__':
    cur.execute("TRUNCATE TABLE metrix")
    
    #cur.execute("DROP TABLE IF EXISTS metrix")
   # cur.execute('CREATE TABLE Metrix ('
#	'ID integer NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
#	'Origin integer NOT NULL,'
#	'Destination integer NOT NULL,'
#	'SeatsNumber integer NOT NULL,'
#	'TimeRequest TIMESTAMP NOT NULL);')

    i = 0
    while 1:
        obj = req()
        obj.gen()
        i += 1

        cur.execute(
            f'''INSERT INTO metrix (origin,destination,seatsnumber,timerequest)
             VALUES ({obj.origin}, {obj.destination}, {obj.SeatNumber}, '{obj.TimeRequest}')''')

        if i == 5000:
            break

con.commit()
print("Record inserted successfully")
con.commit()
con.close()
