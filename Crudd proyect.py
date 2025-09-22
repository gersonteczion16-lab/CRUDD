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


def agregar_p():
    cr.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", 
                (entry_id.get(), entry_nombre.get(), entry_precio.get(), entry_stock.get()))
    baseDeDatos.commit()
    mostrar_p()
    limpiar()


def eliminar_p():
    s = t.selection()
    if s:
        id = t.item(s[0])["values"][0]
        cr.execute("DELETE FROM productos WHERE id=?", (id,))
        baseDeDatos.commit()
        mostrar_p()
        limpiar()

def modificar_p():
    s = t.selection()
    if s:
        cr.execute("UPDATE productos SET nombre=?, precio=?, stock=? WHERE id=?",
                    (entry_nombre.get(), entry_precio.get(), entry_stock.get(), entry_id.get()))
        baseDeDatos.commit()
        mostrar_p()
        limpiar()

