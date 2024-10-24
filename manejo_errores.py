from tkinter import messagebox
import validaciones
from datetime import datetime

def validar_datos(dni, nombre, apellido, edad, fechaDeNacimiento, profesion, monto, fechaDeclarar, origen):
    if not validaciones.es_dni_valido(dni):
        messagebox.showwarning("Error", "El DNI debe ser un número de 7 a 9 dígitos.")
        return None
    elif not validaciones.es_string_valido(apellido):
        messagebox.showwarning("Error", "El apellido debe ser una cadena de texto válida.")
        return None
    elif not validaciones.es_string_valido(nombre):
        messagebox.showwarning("Error", "El nombre debe ser una cadena de texto válida.")
        return None
    elif not edad.isdigit():
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
        return datos