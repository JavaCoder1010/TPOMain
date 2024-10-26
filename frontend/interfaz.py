import tkinter as tk
from frontend.campos import crear_campos_entrada
from frontend.checkboxes import crear_checkboxes
from frontend.botones import configurar_boton_mostrar_datos, agregar_boton_salir
from manejo_errores import validar_datos
from limpiar import limpiar_formulario
from tkinter import messagebox

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

    crear_campos_entrada(ventana, entradas)
    entradas[0].focus_set()
    crear_checkboxes(ventana, variables_bienes_argentina, variables_bienes_exterior)

    def manejar_evento_enviar():
        """
        Maneja el evento de click en el botn "Enviar", recopilando
        los datos de las entradas y los checkboxes, y enviándolos
        a la función enviar_datos.
        """
        enviar_datos(entradas, variables_bienes_argentina, variables_bienes_exterior)

    boton_enviar = tk.Button(ventana, text="Enviar", command=manejar_evento_enviar)
    boton_enviar.grid(row=9, column=1, pady=10)

    configurar_boton_mostrar_datos(ventana)

    agregar_boton_salir(ventana)

    return ventana, boton_enviar


def enviar_datos(entradas, variables_bienes_argentina, variables_bienes_exterior):
    """
    Recolecta los datos de las entradas y los checkboxes, y los valida. Si los datos son válidos,
    los agrega a la lista de datos y muestra un mensaje de éxito. Limpia el formulario y devuelve
    los datos recopilados.

    Args:
        entradas (list): Lista de objetos tk.Entry que contienen los datos de las entradas del formulario.
        variables_bienes_argentina (list): Lista de objetos tk.BooleanVar que contienen los estados de los checkboxes
            de bienes en Argentina.
        variables_bienes_exterior (list): Lista de objetos tk.BooleanVar que contienen los estados de los checkboxes
            de bienes en el exterior.

    Returns:
        list: La lista de datos recopilados, que contiene los datos de las entradas y los estados de los checkboxes.
    """
    datos_formulario = []
    datos_formulario.append(entradas[0].get())  # dni
    datos_formulario.append(entradas[1].get())  # apellido
    datos_formulario.append(entradas[2].get())  # nombre
    datos_formulario.append(entradas[3].get())  # edad
    datos_formulario.append(entradas[4].get())  # fechaDeNacimiento
    datos_formulario.append(entradas[5].get())  # profesion
    datos_formulario.append(entradas[6].get())  # monto
    datos_formulario.append(entradas[7].get())  # fechaDeclarar
    datos_formulario.append(entradas[8].get())  # origen

    # Recolectar estados de los checkboxes
    bienes_argentinos = []
    for var in variables_bienes_argentina:
        bienes_argentinos.append(var.get())

    bienes_exteriores = []
    for var in variables_bienes_exterior:
        bienes_exteriores.append(var.get())

    # Validar los datos
    """
    Valida los datos del formulario y los agrega a la lista de datos si son válidos.

    Args:
        datos_formulario (list): La lista de datos recopilados del formulario, que contiene los datos de las entradas y los estados de los checkboxes.
        variables_bienes_argentina (list): Lista de objetos tk.BooleanVar que contienen los estados de los checkboxes de bienes en Argentina.
        variables_bienes_exterior (list): Lista de objetos tk.BooleanVar que contienen los estados de los checkboxes de bienes en el exterior.

    Returns:
        bool: Verdadero si los datos del formulario son válidos, Falso en caso contrario.
    """
    datos_validos = validar_datos(
        datos_formulario[0],  # dni
        datos_formulario[2],  # nombre
        datos_formulario[1],  # apellido
        datos_formulario[3],  # edad
        datos_formulario[4],  # fechaDeNacimiento
        datos_formulario[5],  # profesion
        datos_formulario[6],  # monto
        datos_formulario[7],  # fechaDeclarar
        datos_formulario[8],  # origen
        bienes_argentinos,
        bienes_exteriores,
    )

    if datos_validos:
        messagebox.showinfo("Éxito", "Datos registrados correctamente")

        # Limpiar el formulario
        limpiar_formulario(
            entradas[0],
            entradas[1],
            entradas[2],
            entradas[3],
            entradas[4],
            entradas[5],
            entradas[6],
            entradas[7],
            entradas[8],
            variables_bienes_argentina,
            variables_bienes_exterior,
        )

        # Agregar los checkboxes a la lista de datos
        datos_formulario.append(bienes_argentinos)
        datos_formulario.append(bienes_exteriores)

        return datos_formulario

    return None