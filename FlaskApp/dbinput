import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="plate",
  database="plates"
)

mycursor = mydb.cursor()
#mycursor.execute("DROP TABLE medewerkers")
#mycursor.execute("DROP TABLE plaat")
#mycursor.execute("DROP DATABASE plates")
#mycursor.execute("CREATE DATABASE plates")
mycursor.execute("CREATE TABLE medewerkers (id INT AUTO_INCREMENT PRIMARY KEY,voornaam VARCHAR(20),achternaam VARCHAR(20), adres VARCHAR(255),functie VARCHAR(25))")
mycursor.execute("CREATE TABLE plaat(id INT AUTO_INCREMENT PRIMARY KEY,nummerplaat VARCHAR(45),actief BOOLEAN,eigenaar_id INT, FOREIGN KEY(eigenaar_id) REFERENCES medewerkers(id))")
mycursor.execute("CREATE TABLE log (id INT AUTO_INCREMENT PRIMARY KEY,tijd_in DATETIME, tijd_uit DATETIME,uitgereden BOOLEAN,plaat_id INT, FOREIGN KEY(plaat_id) REFERENCES plaat(id))")

sql = "INSERT INTO medewerkers (voornaam,achternaam,adres,functie) VALUES (%s, %s, %s, %s)"
val = [
  ('Wouter', 'Vanloocke','Schoonakker', 'netwerkbeheerder'),
  ('Piet', 'Boedt','groenplaats', 'bezoeker'),
  ('Celine', 'Verwilligen','Schoten', 'sysadmin')
]
mycursor.executemany(sql, val)

sql = "INSERT INTO plaat (nummerplaat,actief,eigenaar_id) VALUES (%s, %s, %s)"
val = [
   ('1TQR131',True,1),
   ('1ACN335',False,2),
   ('1ABC123',True,3)
]

mycursor.executemany(sql, val)

mydb.commit() 