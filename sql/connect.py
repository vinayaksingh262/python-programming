import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Vsr2622003*")
print(mydb.connection_id)
