import sqlite3
from tkinter import *
from tkinter import ttk

baseDeDatos = sqlite3.connect("Productos.db")
cur = baseDeDatos.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    precio REAL,
    stock INTEGER
)
""")
baseDeDatos.commit()



