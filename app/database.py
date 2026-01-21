from dotenv import load_dotenv, find_dotenv
import os
import mysql.connector
from typing import List, Dict, Any, cast
from mysql.connector.cursor import MySQLCursorDict

load_dotenv(find_dotenv())

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "LibroNet"),
        port=int(os.getenv("DB_PORT", 3306)),
        charset="utf8mb4"
    )

# =========================
# FETCH ALL
# =========================
def fetch_all_libros() -> List[Dict[str, Any]]:
    conn = None
    try:
        conn = get_connection()
        cur: MySQLCursorDict = conn.cursor(dictionary=True)
        try:
            cur.execute(
                """
                SELECT id_libro, titulo, autor, editorial, isbn,
                       anio_publicacion, categoria, ejemplares, disponible
                FROM libros
                """
            )
            return cast(List[Dict[str, Any]], cur.fetchall())
        finally:
            cur.close()
    finally:
        if conn:
            conn.close()

# =========================
# FETCH BY ID
# =========================
def fetch_libro_by_id(id_libro: int):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute(
            """
            SELECT id_libro, titulo, autor, editorial, isbn,
                   anio_publicacion, categoria, ejemplares, disponible
            FROM libros
            WHERE id_libro = %s
            """,
            (id_libro,)
        )
        return cur.fetchone()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# =========================
# CREATE
# =========================
def create_libro(data: dict) -> int:
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO libros (
                titulo, autor, editorial, isbn,
                anio_publicacion, categoria, ejemplares, disponible
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                data["titulo"],
                data["autor"],
                data.get("editorial"),
                data.get("isbn"),
                data.get("anio_publicacion"),
                data.get("categoria"),
                data["ejemplares"],
                data["disponible"]
            )
        )
        conn.commit()
        return cur.lastrowid
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# =========================
# UPDATE
# =========================
def update_libro(id_libro: int, data: dict) -> bool:
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE libros SET
                titulo=%s,
                autor=%s,
                editorial=%s,
                isbn=%s,
                anio_publicacion=%s,
                categoria=%s,
                ejemplares=%s,
                disponible=%s
            WHERE id_libro=%s
            """,
            (
                data["titulo"],
                data["autor"],
                data.get("editorial"),
                data.get("isbn"),
                data.get("anio_publicacion"),
                data.get("categoria"),
                data["ejemplares"],
                data["disponible"],
                id_libro
            )
        )
        conn.commit()
        return cur.rowcount > 0
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# =========================
# DELETE
# =========================
def delete_libro(id_libro: int) -> bool:
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
