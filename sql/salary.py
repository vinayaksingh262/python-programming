import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Vsr2622003*", database="db1"
)
cur = mydb.cursor()

insalary = "INSERT INTO salary(NAME,BRANCH,ROLL,SALARY) VALUES(%s,%s,%s,%s)"
val = [
    ("saurabh", "EC", "93", "210"),
    ("Nikhil", "CSE", "98", "185"),
    ("Nisha", "CSE", "99", "183"),
    ("Rohan", "MAE", "43", "203"),
    ("Amit", "ECE", "24", "201"),
    ("Anil", "MAE", "45", "209"),
    ("Megha", "ECE", "55", "225"),
    ("Sita", "CSE", "95", "195"),
]

cur.executemany(insalary, val)
mydb.commit()
