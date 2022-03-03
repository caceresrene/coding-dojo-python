from flask import Flask, request, render_template
app = Flask(__name__)

# !
# Solo logre hacer que mostrara tableros de un solor color :c

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<int:matrizCuadrada>')
def tablaCuadrada(matrizCuadrada):
    return render_template('index.html', col=matrizCuadrada, row=matrizCuadrada)


@app.route('/<int:col>/<int:row>')
def tablaPersonalizada(col, row):
    return render_template('index.html', col=col, row=row)


if __name__ == '__main__':
    app.run(debug=True)
