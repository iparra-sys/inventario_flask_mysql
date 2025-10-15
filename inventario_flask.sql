CREATE DATABASE inventario_flask;
USE inventario_flask;

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    cantidad INT,
    precio DECIMAL(10,2)
);
