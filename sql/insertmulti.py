import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Vsr2622003*", database="db1"
)
cur = mydb.cursor()
student = "INSERT INTO student(NAME,BRANCH,ROLL,SECTION,AGE) VALUES(%s,%s,%s,%s,%s)"
val = [
    ("saurabh", "EC", 93, "B", 21),
    ("Nikhil", "CSE", "98", "A", "18"),
    ("Nisha", "CSE", "99", "A", "18"),
    ("Rohan", "MAE", "43", "B", "20"),
    ("Amit", "ECE", "24", "A", "21"),
    ("Anil", "MAE", "45", "B", "20"),
    ("Megha", "ECE", "55", "A", "22"),
    ("Sita", "CSE", "95", "A", "19"),
]
cur.executemany(student, val)
mydb.commit()
