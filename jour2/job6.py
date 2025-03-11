import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user = "root",
  password = "root",
  database = "laplateforme",
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM etudiant;")

results = cursor.fetchall()

results = cursor.fetchone()
cursor.close()
mydb.close()