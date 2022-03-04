from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = '207666459'

@app.route('/')
def home():
  if 'contador' in session and 'visitas' in session:
    session['contador'] += 1
    session['visitas'] += 1
  else:
    session['contador'] = 1
    session['visitas'] = 1
  return render_template('index.html', contador = session['contador'], visitas = session['visitas'])

@app.route('/destroy_session')
def cerrar_sesion():
  session.clear()
  return redirect('/')

@app.route('/2times')
def two_times():
  if 'contador' in session:
    session['contador'] += 1
  else:
    session['contador'] = 1
  return redirect('/')

@app.route('/reinicio')
def reiniciar():
  session['contador'] = 0
  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)