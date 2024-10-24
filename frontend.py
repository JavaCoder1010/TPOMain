from datetime import datetime
import tkinter as tk
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

    # Validar datos usando el archivo de manejo_errores
    datos = manejo_errores.validar_datos(dni, nombre, apellido, edad, fechaDeNacimiento, profesion, monto, fechaDeclarar, origen)

    if datos:
        limpiar_formulario()
        tk.messagebox.showinfo("Éxito", "Datos enviados correctamente.")


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
