import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Vsr2622003*", database="db1"
)

cur = mydb.cursor()
student3 = """CREATE TABLE student3(
NAME VARCHAR(20),
ROLL_NO INT NOT NULL,
MARKS FLOAT)
"""
cur.execute(student3)
val = """INSERT INTO student3 (NAME,ROLL_NO,MARKS) VALUES(%s,%s,%s)
"""
data = ("Vinayak", 65, 85.8)
cur.execute(val, data)
mydb.commit()
print("table created and data inserted successfully")
