import mysql.connector

mydb = mysql.connector.connect(
    user="root", host="localhost", password="Vsr2622003*", database="db1"
)
cur = mydb.cursor()
s = " DROP TABLE student2"
cur.execute(s)
print("table is dropped")
mydb.commit()
mydb.close()
