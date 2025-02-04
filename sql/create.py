import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Vsr2622003*")
cur = mydb.cursor()
cur.execute("CREATE DATABASE db1")
