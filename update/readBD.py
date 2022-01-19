import csv
import psycopg2

con = psycopg2.connect(
    database="postgres",
    user="postgres",  
    password="6675", 
    host="127.0.0.1",
    port="5432"
)
print("Database opened successfully")

    #   копируем в файл данные (время и кол-во мест) из таблицы metrix
    #   исходя из заданных условий (origin и destination)
    
    #   данные сортируются по дате

cur = con.cursor()
cur.execute('COPY (SELECT timerequest, seatsnumber FROM metrix WHERE origin=2 AND destination=5 ORDER BY timerequest)'
            'TO \'D:/1PROPHET/table.csv\' DELIMITER \';\' CSV HEADER');

con.commit()
print("All is good")
con.close()



