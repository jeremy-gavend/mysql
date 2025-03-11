import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user = "root",
  password = "root",
  database = "laplateforme",
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM etage;")

results = cursor.fetchall()

total_superficie = 0
for piece in results:
  total_superficie += piece[3]

# results = cursor.fetchone()

cursor.close()
mydb.close()

print(f"La superficie de La Plateforme est de {total_superficie} m2")