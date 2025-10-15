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
```

---

## ⚙️ Instalación y ejecución

1️⃣ Clonar el repositorio  
```bash
git clone https://github.com/ivethparra/inventario_flask_mysql.git
cd inventario_flask_mysql
```
2️⃣ Crear y activar un entorno virtual
```bash
python -m venv venv
# Activar en Windows:
venv\Scripts\activate
# Activar en Linux/Mac:
source venv/bin/activate
```
3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```
 Crear archivo .env con tus credenciales de MySQL
```bash
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=tu_contraseña
MYSQL_DATABASE=inventario_flask
```
5️⃣ Crear base de datos y tabla
```bash
CREATE DATABASE inventario_flask;
USE inventario_flask;

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    cantidad INT,
    precio DECIMAL(10,2)
);
```
6️⃣ Ejecutar la aplicación
```bash
python app.py

```
7️⃣ Abrir en el navegador
👉 http://localhost:5000

---

## 📸 Capturas de Pantalla

### 🏠 Página principal (Listado de productos)
![Listado de productos](https://github.com/iparra-sys/inventario_flask_mysql/blob/main/static/preview_index.png)

### ➕ Agregar producto
![Agregar producto](https://github.com/iparra-sys/inventario_flask_mysql/blob/main/static/preview_add.png)

### ✏️ Editar producto
![Editar producto](https://github.com/iparra-sys/inventario_flask_mysql/blob/main/static/preview_edit.png)


---

## ⚙️ Funcionalidades principales

✅ **Visualizar productos:** muestra una tabla con todos los registros del inventario.  
➕ **Agregar productos:** formulario con validación básica para ingresar nuevos artículos.  
✏️ **Editar productos:** permite actualizar la información de un producto existente.  
🗑️ **Eliminar productos:** elimina productos de forma permanente del inventario.  
💾 **Conexión MySQL segura:** mediante variables de entorno definidas en el archivo `.env`.  
🎨 **Interfaz moderna y responsive:** construida con Bootstrap 5 y plantillas Jinja2.  
📂 **Estructura clara y modular:** separa la lógica de Flask, las plantillas HTML y los recursos estáticos.

---

## 🚀 Próximas mejoras

Estas son algunas ideas que se planean implementar en futuras versiones del proyecto:

- 🔐 Sistema de **autenticación de usuarios** (login y roles: admin / empleado).  
- 📊 Módulo de **reportes y estadísticas** con gráficos interactivos.  
- 💾 Integración con **subida de archivos CSV** para carga masiva de productos.  
- 🌍 Despliegue del proyecto en **Render o Railway** con base de datos MySQL remota.  
- 🧪 Implementación de **tests automatizados** con `pytest` para garantizar la calidad del código.  
- 🎨 Mejora de la interfaz con **Bootstrap 5** o **Tailwind CSS**.  

---

## 👩‍💻 Autora

**Iveth Parra Herrera**  
Desarrolladora Junior | Python | Flask | MySQL | HTML | CSS | JavaScript  

📫 **Contacto:**  
- 🌐 [LinkedIn](https://www.linkedin.com/in/iveth-parra-herrera-351a6a235)  
- 💻 [GitHub](https://github.com/iparra-sys)

💡 *“El código es una herramienta para construir soluciones reales y dejar huella.”*

✨ Proyecto desarrollado como parte del Portafolio 2025 - Iveth Parra Herrera ✨
