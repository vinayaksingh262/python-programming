import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Vsr2622003*", database="db1"
)
cur = mydb.cursor()
student = """CREATE TABLE student(
NAME VARCHAR(20) NOT NULL,
BRANCH VARCHAR(50),
ROLL  INT NOT NULL,
SECTION VARCHAR(5),
AGE INT )
"""
cur.execute(student)
