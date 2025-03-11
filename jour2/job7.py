import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user = "root",
  password = "root",
  database = "laplateforme",
)

cursor = mydb.cursor()
cursor.execute("USE entreprise;")
cursor.execute("SELECT * FROM employe;")
results = cursor.fetchall()

employes = []



class Employe:
  def __init__(self, nom, prenom, salaire):
    self.nom = nom
    self.prenom = prenom
    self.salaire = salaire

  def __str__(self):
    return f"{self.nom} {self.prenom} gagne {self.salaire}€"
  

cursor.close()
mydb.close()

for employe in results:
    employes.append(Employe(employe[1], employe[2], employe[3]))

print(str(employes[1]))
