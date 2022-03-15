import mysql.connector
from database import cursor
from mysql.connector import errorcode

DB_NAME = 'adoptame'

TABLES = {}

# Crear una tabla nueva TABLE['nombre']
TABLES['comentarios'] = (
  "CREATE TABLE `comentarios` ("
  " `id` int(11) NOT NULL AUTO_INCREMENT,"
  " `usuario` varchar(255) NOT NULL,"
  " `texto` varchar(255) NOT NULL,"
  " `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
  " PRIMARY KEY (`id`)"
  ") ENGINE=InnoDB"
)

TABLES['usuarios'] = (
  "CREATE TABLE `usuarios` ("
  " `id` int(11) NOT NULL AUTO_INCREMENT,"
  " `nombre` varchar(255) NOT NULL,"
  " `edad` smallint UNSIGNED NOT NULL,"
  " `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
  " PRIMARY KEY (`id`)"
  ") ENGINE=InnoDB"
)

# Crear base de datos
def create_database():
  cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
  print(f'👍Database {DB_NAME} created')

# Crear tablas
def create_tables():
  cursor.execute(f'USE {DB_NAME}')
  for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
      print(f'👌Creating table {table_name} ', end='')
      cursor.execute(table_description)
    except mysql.connector.Error as error: 
      if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print('👎Already exists')
      else:
        print(err.msg)

create_database()
create_tables()
# Ver que contiene una tabla
# cursor.execute('DESCRIBE usuarios')
# for x in cursor:
#   print(x)

# cursor.execute('SELECT * FROM usuarios')
# for x in cursor:
#   print(x)