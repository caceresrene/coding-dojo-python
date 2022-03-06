from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'amongus'

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def procesado():
  session['name'] = request.form['name']
  session['favorite'] = request.form['favorite']
  session['location'] = request.form['location']
  session['comment'] = request.form['comment']
  return redirect('/result')

@app.route('/result')
def resultado():
  return render_template('result.html', 
    name = session['name'], 
    favorite = session['favorite'],
    location = session['location'], 
    comment = session['comment'])

if __name__ == '__main__':
	app.run(debug=True)