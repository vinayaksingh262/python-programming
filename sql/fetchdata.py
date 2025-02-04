import mysql.connector

mydb = mysql.connector.connect(
    user="root", host="localhost", password="Vsr2622003*", database="db1"
)
cur = mydb.cursor()
s = "SELECT NAME,MARKS FROM student3 WHERE MARKS>75 "
cur.execute(s)
result = cur.fetchall()
for x in result:
    print(x)
