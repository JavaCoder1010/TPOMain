import tkinter as tk
from tkinter import messagebox
import manejo_errores
import ver_datos
from listas import *
import limpiar

# Variables globales para la ventana y botones
ventana = None
boton_enviar = None
boton_mostrar = None
boton_salir = None
entry_dni = None
entry_apellido = None
entry_nombre = None
entry_edad = None
entry_fechaDeNacimiento = None
entry_profesion = None
entry_monto = None
entry_fechaDeclarar = None
entry_origen = None
variables_bienes_argentina = []
variables_bienes_exterior = []

# Listas para almacenar los datos ingresados
dniLista = []
apellidoLista = []
nombreLista = []
edadLista = []
fechaDeNacimientoLista = []
profesionLista = []
montoLista = []
fechaDeclararLista = []
origenLista = []
bienes_arg_lista = []
bienes_ext_lista = []

def inicializar_interfaz():
    global ventana, boton_enviar, entry_dni, entry_apellido, entry_nombre
    global entry_edad, entry_fechaDeNacimiento, entry_profesion, entry_monto
    global entry_fechaDeclarar, entry_origen

    # VENTANA PRINCIPAL
    ventana = tk.Tk()
    ventana.title("Formulario en Tkinter")

    # CAMPOS DE ENTRADA
    tk.Label(ventana, text="DNI:", anchor=tk.E, width=20).grid(row=0, column=0, sticky=tk.E)
    entry_dni = tk.Entry(ventana, width=30)
    entry_dni.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Apellido:", anchor=tk.E, width=20).grid(row=1, column=0, sticky=tk.E)
    entry_apellido = tk.Entry(ventana, width=30)
    entry_apellido.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Nombre:", anchor=tk.E, width=20).grid(row=2, column=0, sticky=tk.E)
    entry_nombre = tk.Entry(ventana, width=30)
    entry_nombre.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Edad:", anchor=tk.E, width=20).grid(row=3, column=0, sticky=tk.E)
    entry_edad = tk.Entry(ventana, width=30)
    entry_edad.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Fecha de Nacimiento:\n(dd-mm-aaaa)", anchor=tk.E, width=20).grid(row=4, column=0, sticky=tk.E)
    entry_fechaDeNacimiento = tk.Entry(ventana, width=30)
    entry_fechaDeNacimiento.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Profesión:", anchor=tk.E, width=20).grid(row=5, column=0, sticky=tk.E)
    entry_profesion = tk.Entry(ventana, width=30)
    entry_profesion.grid(row=5, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Monto:", anchor=tk.E, width=20).grid(row=6, column=0, sticky=tk.E)
    entry_monto = tk.Entry(ventana, width=30)
    entry_monto.grid(row=6, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Fecha de declaración:\n(dd-mm-aaaa)", anchor=tk.E, width=20).grid(row=7, column=0, sticky=tk.E)
    entry_fechaDeclarar = tk.Entry(ventana, width=30)
    entry_fechaDeclarar.grid(row=7, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Origen de sus fondos:", anchor=tk.E, width=20).grid(row=8, column=0, sticky=tk.E)
    entry_origen = tk.Entry(ventana, width=30)
    entry_origen.grid(row=8, column=1, padx=5, pady=5)

    # Crear frame y checkboxes
    crear_checkboxes()

    # BOTON ENVIAR (sin command inicialmente)
    boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_datos)
    boton_enviar.grid(row=9, column=1, pady=10)

    # BOTON PARA MOSTRAR LOS DATOS
    configurar_boton_mostrar_datos()

    # BOTON SALIR
    agregar_boton_salir()

def crear_checkboxes():
    global variables_bienes_argentina, variables_bienes_exterior

    # FRAME PARA CHECKBOXES
    frame_checkboxes = tk.Frame(ventana)
    frame_checkboxes.grid(row=0, column=2, rowspan=9, padx=10, pady=5)

    # Bienes en Argentina
    tk.Label(frame_checkboxes, text="Bienes en Argentina:").pack(anchor=tk.W)
    nombres_bienes_argentina = [
        "Moneda",
        "Inmuebles",
        "Acciones y participaciones",
        "Títulos valores",
        "Otros bienes muebles",
        "Créditos",
        "Derechos y bienes intangibles",
        "Criptomonedas y criptoactivos",
        "Otros bienes"
    ]

    for nombre in nombres_bienes_argentina:
        var = tk.BooleanVar()
        variables_bienes_argentina.append(var)
        tk.Checkbutton(frame_checkboxes, text=nombre, variable=var).pack(anchor=tk.W)

    # Bienes en el exterior
    tk.Label(frame_checkboxes, text="Bienes en el exterior:").pack(anchor=tk.W)
    nombres_bienes_exterior = [
        "Moneda extranjera",
        "Inmuebles",
        "Acciones y participaciones",
        "Títulos valores",
        "Otros bienes muebles",
        "Créditos",
        "Derechos y bienes intangibles",
        "Otros bienes"
    ]

    for nombre in nombres_bienes_exterior:
        var = tk.BooleanVar()
        variables_bienes_exterior.append(var)
        tk.Checkbutton(frame_checkboxes, text=nombre, variable=var).pack(anchor=tk.W)

def enviar_datos():
    # Recoger datos del formulario
    dni = entry_dni.get()
    apellido = entry_apellido.get()
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    fechaDeNacimiento = entry_fechaDeNacimiento.get()
    profesion = entry_profesion.get()
    monto = entry_monto.get()
    fechaDeclarar = entry_fechaDeclarar.get()
    origen = entry_origen.get()

    # Recoger bienes seleccionados
    bienes_arg = []
    bienes_ext = []

    for var in variables_bienes_argentina:
        bienes_arg.append(var.get())

    for var in variables_bienes_exterior:
        bienes_ext.append(var.get())

    # Validar datos
    datos_validos = manejo_errores.validar_datos(
        dni, nombre, apellido, edad, fechaDeNacimiento,
        profesion, monto, fechaDeclarar, origen,
        bienes_arg, bienes_ext
    )

    if datos_validos:
        messagebox.showinfo("Éxito", "Datos registrados correctamente")

        # Agregar datos a las listas
        dniLista.append(dni)
        apellidoLista.append(apellido)
        nombreLista.append(nombre)
        edadLista.append(edad)
        fechaDeNacimientoLista.append(fechaDeNacimiento)
        profesionLista.append(profesion)
        montoLista.append(monto)
        fechaDeclararLista.append(fechaDeclarar)
        origenLista.append(origen)
        bienes_arg_lista.append(bienes_arg)
        bienes_ext_lista.append(bienes_ext)

        # Limpiar formulario
        limpiar.limpiar_formulario(
            entry_dni, entry_apellido, entry_nombre, entry_edad,
            entry_fechaDeNacimiento, entry_profesion, entry_monto,
            entry_fechaDeclarar, entry_origen,
            variables_bienes_argentina, variables_bienes_exterior
        )
        entry_dni.focus_set()
        return [dni, apellido, nombre, edad, fechaDeNacimiento,
                profesion, monto, fechaDeclarar, origen,
                bienes_arg, bienes_ext]
    return None

def configurar_boton_mostrar_datos():
    global boton_mostrar
    
    # Crear el botón de mostrar
    boton_mostrar = tk.Button(ventana, text="Mostrar Datos", command=lambda: ver_datos.mostrar_datos(
        dniLista,
        apellidoLista,
        nombreLista,
        edadLista,
        fechaDeNacimientoLista,
        profesionLista,
        montoLista,
        fechaDeclararLista,
        origenLista,
        bienes_arg_lista,
        bienes_ext_lista
    ))
    boton_mostrar.grid(row=10, column=1, pady=10)

def agregar_boton_salir():
    global boton_salir
    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.grid(row=11, column=1, pady=10)

# Inicializar la interfaz al importar el módulo
inicializar_interfaz()