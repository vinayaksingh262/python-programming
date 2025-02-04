import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Vsr2622003*", database="db1"
)
cur = mydb.cursor()
q = " SELECT SALARY FROM salary ORDER BY SALARY DESC LIMIT 1, 1"
cur.execute(q)
result = cur.fetchone()

print("The second highest salary is :", result[0])
