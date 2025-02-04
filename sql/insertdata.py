import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Vsr2622003*", database="db1"
)
cur = mydb.cursor()
student = "INSERT INTO student(NAME,BRANCH,ROLL,SECTION,salary) VALUES(%s,%s,%s,%s,%s)"
val = ("Vinayak", "CSECY", 65, "B", 21)
cur.execute(student, val)
mydb.commit()
