import mysql.connector

mydb = mysql.connector.connect(
    user="root", host="localhost", password="Vsr2622003*", database="db1"
)
cur = mydb.cursor()
student3 = """INSERT INTO student3(NAME,ROLL_NO,MARKS) VALUES(%s,%s,%s)
"""
val = [("shanti", 93, 72), ("yamraj", 27, 70), ("pappu", 63, 93)]
cur.executemany(student3, val)
mydb.commit()
print("data inserted")
