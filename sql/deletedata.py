import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Vsr2622003*", database="db1"
)
cur = mydb.cursor()
s = "DELETE FROM student WHERE NAME = 'amit' "
cur.execute(s)
mydb.commit()
mydb.close()
