import sqlite3
from tkinter import *
from tkinter import ttk

# Conexión y creación de tabla
con = sqlite3.connect("Productos.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    precio REAL,
    stock INTEGER
)
""")
con.commit()

# Funciones
def mostrar():
    tabla.delete(*tabla.get_children())
    for fila in cur.execute("SELECT * FROM productos"):
        tabla.insert("", "end", values=fila)

def agregar():
    cur.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", 
                (entry_id.get(), entry_nombre.get(), entry_precio.get(), entry_stock.get()))
    con.commit()
    mostrar()
    limpiar()

def eliminar():
    s = tabla.selection()
    if s:
        id = tabla.item(s[0])["values"][0]
        cur.execute("DELETE FROM productos WHERE id=?", (id,))
        con.commit()
        mostrar()
        limpiar()

def modificar():
    s = tabla.selection()
    if s:
        cur.execute("UPDATE productos SET nombre=?, precio=?, stock=? WHERE id=?",
                    (entry_nombre.get(), entry_precio.get(), entry_stock.get(), entry_id.get()))
        con.commit()
        mostrar()
        limpiar()

def limpiar():
    entry_id.delete(0, END)
    entry_nombre.delete(0, END)
    entry_precio.delete(0, END)
    entry_stock.delete(0, END)

# Interfaz
app = Tk()
app.title("CRUD Productos (Simple)")
app.geometry("400x500")

# Tabla
tabla = ttk.Treeview(app, columns=("ID","Nombre","Precio","Stock"), show="headings")
for col in ("ID","Nombre","Precio","Stock"):
    tabla.heading(col, text=col)
tabla.pack(pady=10)

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

mostrar()
app.mainloop()
con.close()


    

    

