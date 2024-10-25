import tkinter as tk
from tkinter import messagebox  # Importamos messagebox para los alertas
import manejo_errores

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

    # VALIDACION DE DATOS en manejo_errores.py
    datos = manejo_errores.validar_datos(dni, nombre, apellido, edad, fechaDeNacimiento, profesion, monto, fechaDeclarar, origen)

    if datos:
        messagebox.showinfo("Registro exitoso", "Contribuyente registrado exitosamente.")
        return dni, apellido, nombre, edad, fechaDeNacimiento, profesion, monto, fechaDeclarar, origen
    else:
        return None

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

tk.Label(ventana, text="Fecha de Nacimiento:\n(dd-mm-aaaa)").pack(pady=5)
entry_fechaDeNacimiento = tk.Entry(ventana, width=30)
entry_fechaDeNacimiento.pack()

tk.Label(ventana, text="Profesión:").pack(pady=5)
entry_profesion = tk.Entry(ventana, width=30)
entry_profesion.pack()

tk.Label(ventana, text="Monto:").pack(pady=5)
entry_monto = tk.Entry(ventana, width=30)
entry_monto.pack()

tk.Label(ventana, text="Fecha en la que declara sus fondos:\n(dd-mm-aaaa)").pack(pady=5)
entry_fechaDeclarar = tk.Entry(ventana, width=30)
entry_fechaDeclarar.pack()

tk.Label(ventana, text="Origen de sus fondos:").pack(pady=5)
entry_origen = tk.Entry(ventana, width=30)
entry_origen.pack()

# BOTON ENVIAR
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_datos)
boton_enviar.pack(pady=10)

# BOTON SALIR
def agregar_boton_salir():
    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.pack(pady=10)
    
def mostrar_datos(funcion_mostrar, dniLista, apellidoLista, nombreLista, edadLista, fechaDeNacimientoLista, profesionLista, montoLista, fechaDeclararLista, origenLista):
    funcion_mostrar(dniLista, apellidoLista, nombreLista, edadLista, fechaDeNacimientoLista, profesionLista, montoLista, fechaDeclararLista, origenLista)

def configurar_boton_mostrar(funcion_mostrar, dniLista, apellidoLista, nombreLista, edadLista, fechaDeNacimientoLista, profesionLista, montoLista, fechaDeclararLista, origenLista):
    boton_mostrar = tk.Button(ventana, text="Mostrar Datos", command=lambda: mostrar_datos(funcion_mostrar, dniLista, apellidoLista, nombreLista, edadLista, fechaDeNacimientoLista, profesionLista, montoLista, fechaDeclararLista, origenLista))
    boton_mostrar.pack(pady=10)