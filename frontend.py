import tkinter as tk
from tkinter import messagebox
from datetime import datetime



def enviar_datos():
    dni = entry_dni.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    fechaDeNacimiento = entry_fechaDeNacimiento.get()
    profesion = entry_profesion.get()
    monto = entry_monto.get()
    fechaDeclarar = entry_fechaDeclarar.get()
    origen = entry_origen.get()
    

    if dni.isdigit() and apellido and nombre and edad.isdigit() and fechaDeNacimiento and profesion and monto.isdigit() and fechaDeclarar and origen:
        # Muestra los datos en la consola
        (dni, apellido, nombre, int(edad), datetime.strptime(fechaDeNacimiento, '%d-%m-%Y'), profesion, float(monto), datetime.strptime(fechaDeclarar, '%d-%m-%Y'), origen)
        limpiar_formulario()
    else:
        messagebox.showwarning("Error", "Por favor, verifica los campos.")

def limpiar_formulario():
    entry_dni.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_fechaDeNacimiento.delete(0, tk.END)
    entry_profesion.delete(0, tk.END)
    entry_monto.delete(0, tk.END)
    entry_fechaDeclarar.delete(0, tk.END)
    entry_origen.delete(0, tk.END)
    

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario en Tkinter")
ventana.geometry("300x200")

# Etiquetas y campos de entrada
tk.Label(ventana, text="DNI:").pack(pady=5)
entry_dni = tk.Entry(ventana, width=30)
entry_dni.pack()

tk.Label(ventana, text="Apellido:").pack(pady=5)
entry_apellido = tk.Entry(ventana, width=30)
entry_apellido.pack()

tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack()

tk.Label(ventana, text="Edad:").pack(pady=5)
entry_edad = tk.Entry(ventana, width=30)
entry_edad.pack()

tk.Label(ventana, text="Fecha de Nacimiento:").pack(pady=5)
entry_fechaDeNacimiento = tk.Entry(ventana, width=30)
entry_fechaDeNacimiento.pack()

tk.Label(ventana, text="Profesión:").pack(pady=5)
entry_profesion = tk.Entry(ventana, width=30)
entry_profesion.pack()

tk.Label(ventana, text="Monto:").pack(pady=5)
entry_monto = tk.Entry(ventana, width=30)
entry_monto.pack()

tk.Label(ventana, text="Fecha en la que declara sus fondos:").pack(pady=5)
entry_fechaDeclarar = tk.Entry(ventana, width=30)
entry_fechaDeclarar.pack()

tk.Label(ventana, text="Origen de sus fondos:").pack(pady=5)
entry_origen = tk.Entry(ventana, width=30)
entry_origen.pack()


# Botón para enviar los datos
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_datos)
boton_enviar.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
