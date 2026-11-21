from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
def ejercicio1():
    return render_template('ejercicio1.html')
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None

    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = round((nota1 + nota2 + nota3) / 3, 1)

        if promedio >= 40 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)


@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)

