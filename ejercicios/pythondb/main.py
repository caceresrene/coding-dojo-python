from database import cursor, db

def add_comentario(usuario, texto):
  sql = ('INSERT INTO comentarios(usuario, texto) VALUES (%s, %s)')
  cursor.execute(sql, (texto, usuario,))
  db.commit()
  comentario_id = cursor.lastrowid
  print(f'👍Added comentario {comentario_id}')

def get_comentarios():
  sql = ('SELECT * FROM comentarios ORDER BY created_at DESC')
  cursor.execute(sql)
  result = cursor.fetchall()

  for row in result:
    print(row)

def get_comentario(id):
  sql = ('SELECT * FROM comentarios WHERE id = %s')
  cursor.execute(sql, (id,))
  result = cursor.fetchone()

  for row in result:
    print(row)

def update_comentario(id, texto):
  sql = ('UPDATE comentarios SET texto = %s WHERE id = %s')
  cursor.execute(sql, (texto, id,))
  db.commit()
  print(f'👍Comentario updated {id}')

def delete_comentario(id):
  sql = ('DELETE FROM comentarios WHERE id = %s')
  cursor.execute(sql, (id,))
  db.commit()
  print(f'👍Comentario removed {id}')

add_comentario('Este es un comentario', 'Rene')
add_comentario('Este es un otro comentario', 'Joe')
get_comentarios()
get_comentario(2)
update_comentario(2, 'Updated comentario')
delete_comentario(1)