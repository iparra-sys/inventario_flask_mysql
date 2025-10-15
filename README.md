# 🧮 Inventario Flask + MySQL

Aplicación CRUD desarrollada con **Flask** y **MySQL**, que permite gestionar productos de un inventario.  
Incluye funciones para **agregar, editar, eliminar y listar** productos en una interfaz limpia y moderna.

---

## 🚀 Tecnologías utilizadas

- **Python 3**
- **Flask**
- **MySQL**
- **Jinja2**
- **Bootstrap 5**
- **HTML / CSS**

---

## 🧱 Estructura del proyecto

```text
INVENTARIO_FLASK_MYSQL/
│
├── app.py                  # Lógica principal en Flask
├── .env                    # Variables de entorno (no subir al repositorio)
├── requirements.txt        # Dependencias del proyecto
│
├── templates/              # Plantillas HTML (Jinja2)
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   └── edit.html
│
└── static/                 # Archivos estáticos: CSS, imágenes y scripts
    └── style.css


---

## ⚙️ Instalación y ejecución

1️⃣ Clonar el repositorio  
```bash
git clone https://github.com/ivethparra/inventario_flask_mysql.git
cd inventario_flask_mysql
```

---

2️⃣ Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\actívate
```

---

3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

---

4️⃣ Crear archivo .env con tus credenciales de MySQL
```bash
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=tu_contraseña
MYSQL_DATABASE=inventario_flask
```

---

5️⃣ Crear base de datos y tabla

CREATE DATABASE inventario_flask;
USE inventario_flask;

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    cantidad INT,
    precio DECIMAL(10,2)
);

---

6️⃣ Ejecutar la aplicación
```bash
python app.py

```

---

7️⃣ Abrir en el navegador
👉 http://localhost:5000

---

📸 Capturas de pantalla
🖥️ Pantalla principal

➕ Agregar producto

✏️ Editar producto

---

🧩 Funcionalidades
```
✅ CRUD completo (Crear, Leer, Actualizar, Eliminar)
✅ Conexión segura a MySQL mediante variables de entorno
✅ Interfaz moderna con Bootstrap
✅ Validaciones y mensajes visuales de éxito/error
✅ Código modular y fácil de mantener
```
---

👩‍💻 Autor
```
Iveth Parra Herrera
Desarrolladora en formación | Enfocada en Python y desarrollo web
🔗 LinkedIn
🔗 GitHub
```
---

🌱 Próximas mejoras
```
🔐 Sistema de autenticación (login de usuarios)
🔎 Búsqueda y filtros dinámicos
📤 Exportar inventario a CSV
☁️ Despliegue en Render o PythonAnywhere
```
✨ Proyecto desarrollado como parte del Portafolio 2025 - Iveth Parra Herrera ✨
