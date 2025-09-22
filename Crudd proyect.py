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

def limpiar():
    entry_id.delete(0, END)
    entry_nombre.delete(0, END)
    entry_precio.delete(0, END)
    entry_stock.delete(0, END)

#Interfaz

app = Tk()
app.title("CRUD Tabla De Productos")
app.geometry("400x500")

t = ttk.Treeview(app, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
 
for c in ("ID","Nombre","Precio","Stock"):
    t.heading(c, text=c)
    t.grid(pady=10)

Label(app, text="ID").grid()
entry_id = Entry(app); entry_id.grid()

Label(app, text="Nombre").grid()
entry_nombre = Entry(app); entry_nombre.grid()

Label(app, text="Precio").grid()
entry_precio = Entry(app); entry_precio.grid()

Label(app, text="Stock").grid()
entry_stock = Entry(app); entry_stock.grid()

Button(app, text="Agregar", command=agregar_p).grid(pady=5)
Button(app, text="Modificar", command=modificar_p).grid(pady=5)
Button(app, text="Eliminar", command=eliminar_p).grid(pady=5)
Button(app, text="Limpiar", command=limpiar).grid(pady=5)