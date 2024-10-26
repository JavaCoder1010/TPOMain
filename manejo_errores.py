import validaciones
from tkinter import messagebox
from datetime import datetime

def validar_datos(dni, nombre, apellido, edad, fechaDeNacimiento, profesion, monto, fechaDeclarar, origen, bienes_argentinas, bienes_exteriores):
    if not validaciones.es_dni_valido(dni):
        messagebox.showwarning("Error", "El DNI debe ser un número de 7 a 9 dígitos.")
        return None
    elif not validaciones.es_string_valido(apellido):
        messagebox.showwarning("Error", "El apellido debe ser una cadena de texto válida.")
        return None
    elif not validaciones.es_string_valido(nombre):
        messagebox.showwarning("Error", "El nombre debe ser una cadena de texto válida.")
        return None
    elif not validaciones.es_edad_valida(edad):
        messagebox.showwarning("Error", "La edad debe ser un número.")
        return None
    elif not fechaDeNacimiento:
        messagebox.showwarning("Error", "Por favor, ingrese su fecha de nacimiento.")
        return None
    elif not validaciones.es_fecha_valida(fechaDeNacimiento):
        messagebox.showwarning("Error", "La fecha de nacimiento no tiene un formato válido (dd-mm-aaaa).")
        return None
    elif not validaciones.es_string_valido(profesion):
        messagebox.showwarning("Error", "La profesión debe ser una cadena de texto válida.")
        return None
    elif not monto.isdigit():
        messagebox.showwarning("Error", "El monto debe ser un número.")
        return None
    elif not fechaDeclarar:
        messagebox.showwarning("Error", "Por favor, ingrese su fecha de declaración.")
        return None
    elif not validaciones.es_fecha_valida(fechaDeclarar):
        messagebox.showwarning("Error", "La fecha de declaración no tiene un formato válido (dd-mm-aaaa).")
        return None
    elif not validaciones.es_string_valido(origen):
        messagebox.showwarning("Error", "El origen debe ser una cadena de texto válida.")
        return None
    else:
        
        dni_valido = dni
        apellido_valido = apellido
        nombre_valido = nombre
        edad_valida = int(edad)
        fecha_nacimiento_valida = datetime.strptime(fechaDeNacimiento, '%d-%m-%Y')
        profesion_valida = profesion
        monto_valido = float(monto)
        fecha_declaracion_valida = datetime.strptime(fechaDeclarar, '%d-%m-%Y')
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