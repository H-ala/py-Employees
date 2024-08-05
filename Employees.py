import mysql.connector

print('connecting to database')

cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='employees')

print('connected to database')

cursor = cnx.cursor()

query = 'SELECT * FROM information ORDER BY Height DESC, Weight'

cursor.execute(query)

for name, weight, height in cursor:
    print(name, height, weight)
