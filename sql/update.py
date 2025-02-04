import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Vsr2622003*", database="db1"
)
cur = mydb.cursor()
s = "UPDATE student3 SET MARKS=89 WHERE  MARKS=93"
cur.execute(s)
mydb.commit()
