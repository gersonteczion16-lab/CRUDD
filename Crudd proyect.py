import sqlite3
from tkinter import *
from tkinter import ttk

baseDeDatos = sqlite3.connect("Productos.db")
cr = baseDeDatos.cr()
cr.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    precio REAL,
    stock INTEGER
)
""")
baseDeDatos.commit()

def mostrar_p():
    t.delete(*t.get_children())
    for fila in cr.execute("SELECT * FROM productos"):
        t.insert("", "end", values=fila)




