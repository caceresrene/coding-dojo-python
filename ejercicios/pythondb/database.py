import mysql.connector

# sesion de mysql
config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'adoptame'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()