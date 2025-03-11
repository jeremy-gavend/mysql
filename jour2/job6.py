import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user = "root",
  password = "root",
  database = "laplateforme",
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM salle;")

results = cursor.fetchall()

total_capacite = 0
for piece in results:
  total_capacite += piece[3]

# results = cursor.fetchone()

cursor.close()
mydb.close()

print(f"La capacité de La Plateforme est de {total_capacite} personnes")