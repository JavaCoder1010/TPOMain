import tkinter as tk


def limpiar_formulario(
    entry_dni,
    entry_apellido,
    entry_nombre,
    entry_edad,
    entry_fechaDeNacimiento,
    entry_profesion,
    entry_monto,
    entry_fechaDeclarar,
    entry_origen,
    variables_bienes_argentina,
    variables_bienes_exterior,
):
    """
    Limpia todas las entradas y los checkboxes del formulario.
    """
    entry_dni.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_fechaDeNacimiento.delete(0, tk.END)
    entry_profesion.delete(0, tk.END)
    entry_monto.delete(0, tk.END)
    entry_fechaDeclarar.delete(0, tk.END)
    entry_origen.delete(0, tk.END)

    # Limpiar los checkboxes
    for var in variables_bienes_argentina:
        var.set(False)
    for var in variables_bienes_exterior:
        var.set(False)

    entry_dni.focus_set()
