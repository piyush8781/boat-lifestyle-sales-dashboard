import datetime
import time
import random
import pyodbc

try:
    con = pyodbc.connect(r'Driver={SQL SERVER};'
                         r'SERVER=DESKTOP-RQPSSUJ\SQLEXPRESS;'
                         r'Database=boat_project;'
                         r'Trusted_Connection=yes;')

    cursor = con.cursor()

except:
    print('Error occ  while connecting to sql server')

sales_id = list(range(1, 1000))
random.shuffle(sales_id)

while sales_id:
    sale_id = sales_id.pop(0)
    product_key = random.randint(1, 12)
    customer_id = random.randint(101, 201)
    sale_date = datetime.date.today()

    cursor.execute('INSERT INTO sales VALUES (' + str(sale_id) + ', '
                   + str(product_key) + ', '
                   + str(customer_id) + ', '
                   + 'GETDATE())')


    con.commit()
    print(sale_date)
    time.sleep(1)
