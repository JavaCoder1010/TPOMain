import tkinter as tk
from frontend.campos import crear_campos_entrada
from frontend.checkboxes import crear_checkboxes
from frontend.botones import configurar_boton_mostrar_datos, agregar_boton_salir
from manejo_errores import validar_datos
from limpiar import limpiar_formulario
from tkinter import messagebox
from frontend.profesiones import crear_seleccion_profesiones

"""
Variables globales para almacenar entradas y checkboxes en la interfaz.
Estas variables se definen fuera de la función inicializar_interfaz para que
las funciones manejar_evento_enviar y limpiar_formulario puedan acceder a ellas.
"""
entradas = []
variables_bienes_argentina = []
variables_bienes_exterior = []


def inicializar_interfaz():
    """
    Inicializa la interfaz gráfica de usuario con Tkinter, creando la ventana principal
    del formulario. Se generan campos de entrada, checkboxes y botones para interactuar
    con el formulario. Devuelve la ventana y el botón de enviar.

    Returns:
        ventana (tk.Tk): La ventana principal de la interfaz.
        boton_enviar (tk.Button): El botón de enviar asociado al evento manejar_evento_enviar.
    """
    global ventana, entradas, variables_bienes_argentina, variables_bienes_exterior
    ventana = tk.Tk()
    ventana.title("Formulario en Tkinter")

    # Crear campos de entrada una sola vez
    ultima_posicion = crear_campos_entrada(ventana, entradas)
    entradas[0].focus_set()  # Establecer foco en el primer campo

    # Crear selector de profesiones
    profesion_var = crear_seleccion_profesiones(ventana, ultima_posicion)
    # Agregamos la variable de profesión a entradas
    entradas.append(profesion_var)

    # Crear checkboxes después del selector de profesiones
    crear_checkboxes(ventana, variables_bienes_argentina, variables_bienes_exterior)

    def manejar_evento_enviar():
        """
        Maneja el evento de click en el botón "Enviar", recopilando
        los datos de las entradas y los checkboxes, y enviándolos
        a la función enviar_datos.
        """
        enviar_datos(entradas, variables_bienes_argentina, variables_bienes_exterior)

    boton_enviar = tk.Button(ventana, text="Enviar", command=manejar_evento_enviar)
    boton_enviar.grid(row=ultima_posicion + 1, column=1, pady=10)

    configurar_boton_mostrar_datos(ventana)
    agregar_boton_salir(ventana)

    return ventana, boton_enviar


def enviar_datos(entradas, variables_bienes_argentina, variables_bienes_exterior):
    """
    Recolecta los datos de las entradas y los checkboxes, y los valida.
    """
    datos_formulario = []

    # DNI
    dni = entradas[0].get().strip() if isinstance(entradas[0], tk.Entry) else ""
    datos_formulario.append(dni)

    # Apellido
    apellido = entradas[1].get().strip() if isinstance(entradas[1], tk.Entry) else ""
    datos_formulario.append(apellido)

    # Nombre
    nombre = entradas[2].get().strip() if isinstance(entradas[2], tk.Entry) else ""
    datos_formulario.append(nombre)

    # Edad
    edad = entradas[3].get().strip() if isinstance(entradas[3], tk.Entry) else ""
    datos_formulario.append(edad)

    # Fecha de Nacimiento
    fecha_nac = entradas[4].get().strip() if isinstance(entradas[4], tk.Entry) else ""
    datos_formulario.append(fecha_nac)

    # Monto
    monto = entradas[5].get().strip() if isinstance(entradas[5], tk.Entry) else ""
    datos_formulario.append(monto)

    # Fecha Declarar
    fecha_dec = entradas[6].get().strip() if isinstance(entradas[6], tk.Entry) else ""
    datos_formulario.append(fecha_dec)

    # Origen
    origen = entradas[7].get().strip() if isinstance(entradas[7], tk.Entry) else ""
    datos_formulario.append(origen)

    # Profesión (último elemento de entradas)
    profesion_var = entradas[-1]

    # Recolectar estados de los checkboxes
    bienes_argentinos = []
    for var in variables_bienes_argentina:
        bienes_argentinos.append(var.get())

    bienes_exteriores = []
    for var in variables_bienes_exterior:
        bienes_exteriores.append(var.get())

    # Validar los datos
    datos_validos = validar_datos(
        dni,  # dni
        nombre,  # nombre
        apellido,  # apellido
        edad,  # edad
        fecha_nac,  # fechaDeNacimiento
        profesion_var,  # profesion_var
        monto,  # monto
        fecha_dec,  # fechaDeclarar
        origen,  # origen
        bienes_argentinos,
        bienes_exteriores,
    )

    if datos_validos:
        messagebox.showinfo("Éxito", "Datos registrados correctamente")

        # Llamada corregida a limpiar_formulario
        limpiar_formulario(
            entradas[0],  # DNI
            entradas[1],  # Apellido
            entradas[2],  # Nombre
            entradas[3],  # Edad
            entradas[4],  # Fecha de Nacimiento
            entradas[5],  # Monto
            entradas[6],  # Fecha Declarar
            entradas[7],  # Origen
            entradas[-1],  # Profesión (último elemento)
            variables_bienes_argentina,
            variables_bienes_exterior,
        )
        return datos_validos

    return None
