from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = "clave_secreta_iveth"  # Puedes poner cualquier valor

# Conexión a MySQL
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        port=os.getenv("MYSQL_PORT"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        use_pure=True
    )
    return connection



# Ruta principal (listar productos)
@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM productos")
    items = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', items=items)


# Agregar producto
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        cantidad = request.form['cantidad']
        precio = request.form['precio']

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO productos (nombre, categoria, cantidad, precio)
            VALUES (%s, %s, %s, %s)
        """, (nombre, categoria, cantidad, precio))
        connection.commit()
        cursor.close()
        connection.close()
        flash("✅ Producto agregado con éxito", "success")
        return redirect('/')
    
    # Reutiliza el mismo formulario
    return render_template('form.html', producto=None)


# Editar producto
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        cantidad = request.form['cantidad']
        precio = request.form['precio']

        cursor.execute("""
            UPDATE productos 
            SET nombre=%s, categoria=%s, cantidad=%s, precio=%s 
            WHERE id=%s
        """, (nombre, categoria, cantidad, precio, id))
        connection.commit()
        cursor.close()
        connection.close()
        flash("✏️ Producto actualizado correctamente", "info")
        return redirect('/')

    cursor.execute("SELECT * FROM productos WHERE id=%s", (id,))
    producto = cursor.fetchone()
    cursor.close()
    connection.close()
    return render_template('form.html', producto=producto)



# Eliminar producto
@app.route('/delete/<int:id>')
def delete(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM productos WHERE id=%s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    flash("🗑️ Producto eliminado con éxito", "danger")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

