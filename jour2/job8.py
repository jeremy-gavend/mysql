import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user = "root",
  password = "root",
  database = "laplateforme",
)

cursor = mydb.cursor()

cursor.execute("SHOW DATABASES;")
databases = cursor.fetchall()

already_exists = False
for database in databases:
    if database[0] == "zoo":
        already_exists = True
        break

if not already_exists:
    cursor.execute("CREATE DATABASE zoo;")

cursor.execute("USE zoo;")

# cursor.execute("SHOW TABLES;")
# tables = cursor.fetchall()

# tables_exists = False
# for table in tables:
#     if table[0] == "animal" or table[0] == "cage":
#         tables_exists == True
#         break

# if not tables_exists:
try:
    cursor.execute("CREATE TABLE animal(id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), race VARCHAR(255), id_cage INT, date_naissance VARCHAR(255), pays VARCHAR(255));")
except Exception:
    print("Table \"animal\" already exist!")

try:
    cursor.execute("CREATE TABLE cage(id INT AUTO_INCREMENT PRIMARY KEY, superficie INT, capacite INT, animal_id INT);")
except Exception:
    print("Table \"cage\" already exist!")

def show_animals():
    cursor.execute("SELECT * FROM animal;")
    results = cursor.fetchall()
    for animal in results:
        print(animal)

def show_animals_in_cage():
    cursor.execute(f"SELECT cage.id, animal.nom FROM cage LEFT JOIN animal on animal.id = cage.id;")
    results = cursor.fetchall()
    for animal in results:
        print(animal)

def manage_cages():
    answer = input("Directeur, voulez-vous (a)jouter, (m)odifier ou (s)upprimer une cage? ou (q)uitter? ")
    match answer:
        case "a" | "ajouter":
            cage_size = int(input("Superficie de la cage: "))
            cage_capacity = int(input("Capacité de la cage: "))
            cursor.execute(f"INSERT INTO cage(superficie, capacite) VALUES({cage_size}, {cage_capacity});")
            
            return True
                           
        case "m" | "modifier":
            show_animals_in_cage()
            cage_id = int(input("Quelle cage voulez-vous modifier? "))
            cage_new_size = int(input("Nouvelle superficie de la cage: "))
            cage_new_capacity = int(input("Nouvelle capacité de la cage: "))
            cursor.execute(f" \
                UPDATE cage SET superficie = {cage_new_size}, \
                capacite = {cage_new_capacity} \
                WHERE {cage_id} = id; \
                ")
            
            return True
        
        case "s" | "supprimer":
            show_animals_in_cage()
            cage_id = int(input("Quelle cage voulez-vous supprimer? "))
            cursor.execute(f"DELETE * FROM cage WHERE {cage_id} = id;")
            print("Cage supprimée avec succes!")

            return True
        
        case _:
            print("Au revoir!")
            return False

def manage_animals():
    answer = input("Directeur, voulez-vous (a)jouter, (m)odifier ou (s)upprimer un animal? ou (q)uitter? ")
    match answer:
        case "a" | "ajouter":
            animal_name = input("Nom de l'animal: ")
            animal_race = input("Race de l'animal: ")
            animal_cage = int(input("Cage de l'animal: "))
            animal_birth = input("Date de naissance de l'animal: ")
            animal_country = input("Pays de l'animal: ")
            cursor.execute(f"INSERT INTO animal(nom, race, id_cage, date_naissance, pays) VALUES('{animal_name}', '{animal_race}', {animal_cage}, '{animal_birth}', '{animal_country}');")
            
            return True
                           
        case "m" | "modifier":
            show_animals()
            animal_name = input("Quel animal voulez-vous modifier? ")
            animal_new_name = input("Nouveau nom de l'animal: ")
            animal_race = input("Nouvelle race de l'animal: ")
            animal_cage = int(input("Cage de l'animal: "))
            animal_birth = datetime.date(input("Date de naissance de l'animal: "))
            animal_country = input("Pays de l'animal: ")
            cursor.execute(f" \
                UPDATE animal SET nom = {animal_new_name}, \
                race = {animal_race}, \
                id_cage = {animal_cage}, \
                date_naissance = {animal_birth}, \
                pays = {animal_country} \
                WHERE name = {animal_name}; \
                ")
            
            return True
        
        case "s" | "supprimer":
            show_animals()
            animal_name = input("Quel animal voulez-vous supprimer? ")
            cursor.execute(f"DELETE * FROM animal WHERE name = {animal_name};")
            print("Animal supprimé avec succes!")

            return True
        
        case _:
            print("Au revoir!")
            return False

def calculate_total_size():
    cursor.execute("SELECT superficie FROM cage;")
    results = cursor.fetchall()
    total_size = 0
    for cage in results:
        total_size += cage[0]
    return total_size

running = True
while running:
    show_animals()
    show_animals_in_cage()
    calculate_total_size()

    running = manage_cages()
    running = manage_animals()

cursor.close()
mydb.close()