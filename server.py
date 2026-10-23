from flask import Flask, render_template

app = Flask(_name_)

@app.route('/home')
def home():
    return render_template('index.html', titulo='Home', mensaje='Bienvenido a la página de inicio de UDL-ICO')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='Servicios', mensaje='Servicios ofrecidos')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', titulo='Contacto', mensaje='Contáctanos para más información')

@app.route('/productos')
def productos():
    return render_template('productos.html', titulo='Productos', mensaje='Productos disponibles')

if _name_ == '_main_':
    app.run(debug=True, port=5050)