import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Vsr2622003*", database="db1"
)
cur = mydb.cursor()
s = " SELECT * FROM student3  LIMIT 1,2"
cur.execute(s)
result = cur.fetchall()
for x in result:
    print(x)
