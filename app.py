from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mendez.2020',
    'database': 'login_system'
}

# Ruta principal (formulario de login)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Conexión a MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Verificar credenciales
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if user:
            # Si las credenciales son correctas, redirige a pagina1.html
            return redirect(url_for('pagina1'))
        else:
            return render_template('index.html', error="Usuario o contraseña incorrectos")
    
    return render_template('index.html')

# Ruta para pagina1.html
@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')

if __name__ == '__main__':
    app.run(debug=True)
