# limpiar.py

import tkinter as tk


def limpiar_formulario(
    entry_dni,
    entry_apellido,
    entry_nombre,
    entry_edad,
    entry_fechaDeNacimiento,
    entry_monto,
    entry_fechaDeclarar,
    entry_origen,
    profesion_var,  # Agregamos la variable de profesión
    variables_bienes_argentina,
    variables_bienes_exterior,
):
    """
    Limpia todas las entradas y los checkboxes del formulario.
    """
    # Limpiar campos de entrada
    entry_dni.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_fechaDeNacimiento.delete(0, tk.END)
    entry_monto.delete(0, tk.END)
    entry_fechaDeclarar.delete(0, tk.END)
    entry_origen.delete(0, tk.END)

    # Limpiar selección de profesión
    profesion_var.set("")  # Limpia la selección del radiobutton

    # Limpiar los checkboxes
    for var in variables_bienes_argentina:
        var.set(False)
    for var in variables_bienes_exterior:
        var.set(False)

    # Establecer el foco en el primer campo
    entry_dni.focus_set()
