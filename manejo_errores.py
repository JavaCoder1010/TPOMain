import validaciones
from tkinter import messagebox
from datetime import datetime


def validar_datos(
    dni,
    nombre,
    apellido,
    edad,
    fechaDeNacimiento,
    profesion,
    monto,
    fechaDeclarar,
    origen,
    bienes_argentinas,
    bienes_exteriores,
):
    """
    Valida los datos de entrada del formulario y muestra advertencias si hay errores.

    La función verifica la validez de cada campo de entrada, utilizando funciones de validación específicas para el DNI,
    cadenas de texto, edades, fechas y montos. Si algún campo no es válido, se muestra un mensaje de advertencia y se
    interrumpe la validación. Si todos los campos son válidos, se formatean y agrupan en una lista para su registro.

    Args:
        dni (str): El DNI del usuario, debe ser un número de 7 a 9 dígitos.
        nombre (str): El nombre del usuario, debe ser una cadena de texto válida.
        apellido (str): El apellido del usuario, debe ser una cadena de texto válida.
        edad (str): La edad del usuario, debe ser un número entre 18 y 100.
        fechaDeNacimiento (str): La fecha de nacimiento en formato 'dd-mm-aaaa'.
        profesion (str): La profesión del usuario, debe ser una cadena de texto válida.
        monto (str): El monto, debe ser un número.
        fechaDeclarar (str): La fecha de declaración en formato 'dd-mm-aaaa'.
        origen (str): El origen de los fondos, debe ser una cadena de texto válida.
        bienes_argentinas (list): Lista de estados de checkboxes de bienes en Argentina.
        bienes_exteriores (list): Lista de estados de checkboxes de bienes en el exterior.

    Returns:
        list: Una lista de datos validados si todos los campos son válidos, None en caso contrario.
    """
    if not validaciones.es_dni_valido(dni):
        messagebox.showwarning("Error", "El DNI debe ser un número de 7 a 9 dígitos.")
        return None
    elif not validaciones.es_string_valido(apellido):
        messagebox.showwarning(
            "Error", "El apellido debe ser una cadena de texto válida."
        )
        return None
    elif not validaciones.es_string_valido(nombre):
        messagebox.showwarning(
            "Error", "El nombre debe ser una cadena de texto válida."
        )
        return None
    elif not validaciones.es_edad_valida(edad):
        messagebox.showwarning("Error", "La edad debe ser un número.")
        return None
    elif not fechaDeNacimiento:
        messagebox.showwarning("Error", "Por favor, ingrese su fecha de nacimiento.")
        return None
    elif not validaciones.es_fecha_valida(fechaDeNacimiento):
        messagebox.showwarning(
            "Error", "La fecha de nacimiento no tiene un formato válido (dd-mm-aaaa)."
        )
        return None
    elif not validaciones.es_string_valido(profesion):
        messagebox.showwarning(
            "Error", "La profesión debe ser una cadena de texto válida."
        )
        return None
    elif not monto.isdigit():
        messagebox.showwarning("Error", "El monto debe ser un número.")
        return None
    elif not fechaDeclarar:
        messagebox.showwarning("Error", "Por favor, ingrese su fecha de declaración.")
        return None
    elif not validaciones.es_fecha_valida(fechaDeclarar):
        messagebox.showwarning(
            "Error", "La fecha de declaración no tiene un formato válido (dd-mm-aaaa)."
        )
        return None
    elif not validaciones.es_string_valido(origen):
        messagebox.showwarning(
            "Error", "El origen debe ser una cadena de texto válida."
        )
        return None
    else:

        dni_valido = dni
        apellido_valido = apellido
        nombre_valido = nombre
        edad_valida = int(edad)
        fecha_nacimiento_valida = datetime.strptime(fechaDeNacimiento, "%d-%m-%Y")
        profesion_valida = profesion
        monto_valido = float(monto)
        fecha_declaracion_valida = datetime.strptime(fechaDeclarar, "%d-%m-%Y")
        origen_valido = origen
        bienes_argentinas_validos = bienes_argentinas
        bienes_exteriores_validos = bienes_exteriores

        datos = [
            dni_valido,
            apellido_valido,
            nombre_valido,
            edad_valida,
            fecha_nacimiento_valida,
            profesion_valida,
            monto_valido,
            fecha_declaracion_valida,
            origen_valido,
            bienes_exteriores_validos,
            bienes_argentinas_validos,
        ]

        print("Datos a registrar:", datos)  # Mensaje de depuración
        return datos
