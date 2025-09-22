
import sqlite3
from tkinter import *
from tkinter import ttk

# Conexión a la base de datos
conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    precio REAL,
    stock INTEGER
)
""")
conexion.commit()

# --- Funciones ---
def mostrar():
    tabla.delete(*tabla.get_children())
    for fila in cursor.execute("SELECT * FROM productos"):
        tabla.insert("", "end", values=fila)

def agregar():
    id = int(entry_id.get())
    nombre = entry_nombre.get()
    precio = float(entry_precio.get())
    stock = int(entry_stock.get())
    cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", (id, nombre, precio, stock))
    conexion.commit()
    mostrar()
    limpiar()

def eliminar():
    sel = tabla.selection()
    if sel:
        id = tabla.item(sel[0])["values"][0]
        cursor.execute("DELETE FROM productos WHERE id=?", (id,))
        conexion.commit()
        mostrar()
        limpiar()

def cargar(e):
    sel = tabla.selection()
    if sel:
        id, nombre, precio, stock = tabla.item(sel[0])["values"]
        entry_id.delete(0, END); entry_id.insert(0, id)
        entry_nombre.delete(0, END); entry_nombre.insert(0, nombre)
        entry_precio.delete(0, END); entry_precio.insert(0, precio)
        entry_stock.delete(0, END); entry_stock.insert(0, stock)

def modificar():
    sel = tabla.selection()
    if sel:
        id = int(entry_id.get())
        nombre = entry_nombre.get()
        precio = float(entry_precio.get())
        stock = int(entry_stock.get())
        cursor.execute("UPDATE productos SET nombre=?, precio=?, stock=? WHERE id=?",
                       (nombre, precio, stock, id))
        conexion.commit()
        mostrar()
        limpiar()

def limpiar():
    entry_id.delete(0, END)
    entry_nombre.delete(0, END)
    entry_precio.delete(0, END)
    entry_stock.delete(0, END)

# --- Interfaz ---
app = Tk()
app.title("CRUD con SQLite (Simple)")
app.geometry("400x500")

# Tabla
tabla = ttk.Treeview(app, columns=("ID","Nombre","Precio","Stock"), show="headings")
for col in ("ID","Nombre","Precio","Stock"):
    tabla.heading(col, text=col)
    tabla.column(col, width=80, anchor="center")
tabla.pack(pady=10)
tabla.bind("<<TreeviewSelect>>", cargar)

# Entradas
Label(app, text="ID").pack()
entry_id = Entry(app); entry_id.pack()

Label(app, text="Nombre").pack()
entry_nombre = Entry(app); entry_nombre.pack()

Label(app, text="Precio").pack()
entry_precio = Entry(app); entry_precio.pack()

Label(app, text="Stock").pack()
entry_stock = Entry(app); entry_stock.pack()

# Botones
Button(app, text="Agregar", command=agregar).pack(pady=5)
Button(app, text="Modificar", command=modificar).pack(pady=5)
Button(app, text="Eliminar", command=eliminar).pack(pady=5)
Button(app, text="Limpiar", command=limpiar).pack(pady=5)

# Mostrar al inicio
mostrar()
app.mainloop()

# Cerrar conexión
conexion.close()
