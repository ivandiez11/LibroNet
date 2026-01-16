from dotenv import load_dotenv, find_dotenv
import os
import mysql.connector
from typing import List, Dict, Any, cast
from mysql.connector.cursor import MySQLCursorDict

# Cargar variables de entorno desde .env
load_dotenv(find_dotenv())

def get_connection():
    """Devuelve una conexión a la base de datos MySQL"""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "LibroNet"),
        port=int(os.getenv("DB_PORT", 3306)),
        charset="utf8mb4"
    )


def fetch_all_libros() -> List[Dict[str, Any]]:
    """Obtiene todos los libros de la base de datos"""
    conn = None
    try:
        conn = get_connection()
        cur: MySQLCursorDict = conn.cursor(dictionary=True)
        try:
            cur.execute(
                """
                SELECT id_libro, titulo, autor, editorial, isbn,
                       anio_publicacion, categoria, ejemplares, disponible
                FROM libros;
                """
            )
            rows = cast(List[Dict[str, Any]], cur.fetchall())
            return rows
        finally:
            cur.close()
    finally:
        if conn:
            conn.close()

# ==========================
# ELIMINAR LIBRO
# ==========================
def delete_libro(id_libro: int) -> bool:
    """
    Elimina un libro por su ID.
    Devuelve True si se eliminó, False si no existía.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM libros WHERE id_libro = %s", (id_libro,))
        conn.commit()
        return cur.rowcount > 0
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
