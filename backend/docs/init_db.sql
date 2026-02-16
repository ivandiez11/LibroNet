-- 1️⃣ Borrar la base de datos si ya existe
DROP DATABASE IF EXISTS libroNet;

-- 2️⃣ Crear una nueva base de datos
CREATE DATABASE libroNet CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- 3️⃣ Seleccionar la base de datos recién creada
USE libroNet;

-- 4️⃣ Crear la tabla 'libros'
CREATE TABLE libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    editorial VARCHAR(100),
    isbn VARCHAR(20) UNIQUE,
    anio_publicacion YEAR,
    categoria VARCHAR(50),
    ejemplares INT NOT NULL DEFAULT 1,
    disponible BOOLEAN NOT NULL DEFAULT TRUE
);

-- 5️⃣ Insertar algunos registros de ejemplo
INSERT INTO libros 
(titulo, autor, editorial, isbn, anio_publicacion, categoria, ejemplares, disponible)
VALUES
('Cien Años de Soledad', 'Gabriel García Márquez', 'Editorial Sudamericana', '978-3-16-148410-0', 1967, 'Novela', 5, TRUE),
('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Francisco de Robles', '978-1-56619-909-4', 1605, 'Novela', 3, TRUE),
('La Sombra del Viento', 'Carlos Ruiz Zafón', 'Planeta', '978-84-08-05712-6', 2001, 'Misterio', 4, TRUE),
('1984', 'George Orwell', 'Secker & Warburg', '978-0-452-28423-4', 1949, 'Distopía', 6, TRUE),
('El Principito', 'Antoine de Saint-Exupéry', 'Reynal & Hitchcock', '978-0-15-601219-5', 1943, 'Fantasía', 7, TRUE);


-- 6️⃣ Confirmar
SELECT * FROM libros;