from tkinter import *
from tkinter import ttk

# Lista de productos (ID, Nombre, Precio, Stock)
productos = [
    [1, "Laptop", 1200, 5],
    [2, "Mouse", 25, 50],
    [3, "Teclado", 45, 30]
]

# Funciones
def mostrar_productos():
    tabla.delete(*tabla.get_children())
    for p in productos:
        tabla.insert("", "end", values=p)

def agregar_producto():
    try:
        id = int(entry_id.get())
        nombre = entry_nombre.get()
        precio = float(entry_precio.get())
        stock = int(entry_stock.get())
        productos.append([id, nombre, precio, stock])
        mostrar_productos()
        limpiar_campos()
    except:
        print("Error al agregar")

def eliminar_producto():
    seleccionado = tabla.selection()
    if seleccionado:
        valores = tabla.item(seleccionado[0])["values"]
        productos[:] = [p for p in productos if p[0] != valores[0]]
        mostrar_productos()

def cargar_producto():
    seleccionado = tabla.selection()
    if seleccionado:
        valores = tabla.item(seleccionado[0])["values"]
        entry_id.delete(0, END)
        entry_nombre.delete(0, END)
        entry_precio.delete(0, END)
        entry_stock.delete(0, END)
        entry_id.insert(0, valores[0])
        entry_nombre.insert(0, valores[1])
        entry_precio.insert(0, valores[2])
        entry_stock.insert(0, valores[3])

def modificar_producto():
    seleccionado = tabla.selection()
    if seleccionado:
        try:
            id_nuevo = int(entry_id.get())
            nombre_nuevo = entry_nombre.get()
            precio_nuevo = float(entry_precio.get())
            stock_nuevo = int(entry_stock.get())
            valores = tabla.item(seleccionado[0])["values"]
            for i in range(len(productos)):
                if productos[i][0] == valores[0]:
                    productos[i] = [id_nuevo, nombre_nuevo, precio_nuevo, stock_nuevo]
                    break
            mostrar_productos()
            limpiar_campos()
        except:
            print("Error al modificar")

def limpiar_campos():
    entry_id.delete(0, END)
    entry_nombre.delete(0, END)
    entry_precio.delete(0, END)
    entry_stock.delete(0, END)

# Interfaz
app = Tk()
app.title("Productos CRUD")
app.geometry("400x500")

# Tabla
tabla = ttk.Treeview(app, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
for col in ("ID", "Nombre", "Precio", "Stock"):
    tabla.heading(col, text=col)
    tabla.column(col, width=80, anchor="center")
tabla.pack(pady=10)
tabla.bind("<<TreeviewSelect>>", lambda e: cargar_producto())

# Entradas
Label(app, text="ID").pack()
entry_id = Entry(app)
entry_id.pack()

Label(app, text="Nombre").pack()
entry_nombre = Entry(app)
entry_nombre.pack()

Label(app, text="Precio").pack()
entry_precio = Entry(app)
entry_precio.pack()

Label(app, text="Stock").pack()
entry_stock = Entry(app)
entry_stock.pack()

# Botones
Button(app, text="Agregar", command=agregar_producto).pack(pady=5)
Button(app, text="Modificar", command=modificar_producto).pack(pady=5)
Button(app, text="Eliminar", command=eliminar_producto).pack(pady=5)
Button(app, text="Limpiar", command=limpiar_campos).pack(pady=5)

mostrar_productos()
app.mainloop()
