from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def home():
  query = 'SELECT * FROM comentarios;'
  result = connectToMySQL('adoptame').query_db(query)
  return render_template('index.html', result=result)

@app.route('/insert')
def insert():
  data = {
    'usuario': 'Pedro',
    'texto': 'Esto es un comentario nuevo'
  }
  query = 'INSERT INTO comentarios (usuario, texto) VALUES(%(usuario)s, %(texto)s)'
  result = connectToMySQL('adoptame').query_db(query, data)
  return render_template('insert.html', result=result)

@app.route('/delete/<int:id>')
def delete(id):
  data = {
    'id': id
  }
  query = 'DELETE FROM comentarios WHERE id = %(id)s;'
  result = connectToMySQL('adoptame').query_db(query, data)
  return redirect('/')

@app.route('/update_comentario/<int:id>/<texto>')
def update(id, texto):
  print('👌')
  data = {
    'id': id,
    'texto': texto
  }
  query = 'UPDATE comentarios SET texto =%(texto)s WHERE id=%(id)s'
  result = connectToMySQL('adoptame').query_db(query, data)
  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)