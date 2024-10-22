from datetime import datetime
import tkinter as tk
from tkinter import messagebox

dniLista = []
apellidoLista = []
nombreLista = []
edadLista = []
fechaDeNacimientoLista = []
profesionLista = []
montoLista = []
fechaDeclararLista = []
origenLista = []


def es_fecha_valida(fecha_str, formato='%d-%m-%Y'):
    try:
        datetime.strptime(fecha_str, formato)
        return True
    except ValueError:
        return False

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

    # Validación de los datos ingresados
    if not dni.isdigit() and len(dni) < 7 and len(dni) >= 9: 
        messagebox.showwarning("Error", "El DNI debe ser un número.")
        return None
    elif not apellido:
        messagebox.showwarning("Error", "Por favor, ingrese su apellido.")
        return None
    elif not nombre:
        messagebox.showwarning("Error", "Por favor, ingrese su nombre.")
        return None
    elif not edad.isdigit():
        messagebox.showwarning("Error", "La edad debe ser un número.")
        return None
    elif not fechaDeNacimiento:
        messagebox.showwarning("Error", "Por favor, ingrese su fecha de nacimiento.")
        return None
    elif not es_fecha_valida(fechaDeNacimiento):
        messagebox.showwarning("Error", "La fecha de nacimiento no tiene un formato válido (dd-mm-aaaa).")
        return None
    elif not profesion:
        messagebox.showwarning("Error", "Por favor, ingrese su profesion.")
        return None
    elif not monto.isdigit():
        messagebox.showwarning("Error", "El monto debe ser un número.")
        return None
    elif not fechaDeclarar:
        messagebox.showwarning("Error", "Por favor, ingrese su fecha de declaración.")
        return None
    elif not es_fecha_valida(fechaDeclarar):
        messagebox.showwarning("Error", "La fecha de declaración no tiene un formato válido (dd-mm-aaaa).")
        return None
    elif not origen:
        messagebox.showwarning("Error", "Por favor, ingrese el origen de sus fondos.")
        return None
    else:
        # Convertimos los campos a sus tipos correctos ahora que hemos validado los datos
        datos = (
            dni,
            apellido,
            nombre,
            int(edad),
            datetime.strptime(fechaDeNacimiento, '%d-%m-%Y'),
            profesion,
            float(monto),
            datetime.strptime(fechaDeclarar, '%d-%m-%Y'),
            origen
        )
        limpiar_formulario()
        
        return datos

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
ventana.geometry("300x700")

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

tk.Label(ventana, text="Fecha de Nacimiento (dd-mm-aaaa):").pack(pady=5)
entry_fechaDeNacimiento = tk.Entry(ventana, width=30)
entry_fechaDeNacimiento.pack()

tk.Label(ventana, text="Profesión:").pack(pady=5)
entry_profesion = tk.Entry(ventana, width=30)
entry_profesion.pack()

tk.Label(ventana, text="Monto:").pack(pady=5)
entry_monto = tk.Entry(ventana, width=30)
entry_monto.pack()

tk.Label(ventana, text="Fecha en la que declara sus fondos (dd-mm-aaaa):").pack(pady=5)
entry_fechaDeclarar = tk.Entry(ventana, width=30)
entry_fechaDeclarar.pack()

tk.Label(ventana, text="Origen de sus fondos:").pack(pady=5)
entry_origen = tk.Entry(ventana, width=30)
entry_origen.pack()

# Botón para enviar los datos
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_datos)
boton_enviar.pack(pady=10)

# Botón para salir del programa
boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
boton_salir.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
