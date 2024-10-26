import tkinter as tk

def limpiar_formulario(entry_dni, entry_apellido, entry_nombre, entry_edad, entry_fechaDeNacimiento, entry_profesion, entry_monto, entry_fechaDeclarar, entry_origen, variables_bienes_argentina, variables_bienes_exterior):
    entry_dni.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_fechaDeNacimiento.delete(0, tk.END)
    entry_profesion.delete(0, tk.END)
    entry_monto.delete(0, tk.END)
    entry_fechaDeclarar.delete(0, tk.END)
    entry_origen.delete(0, tk.END)

    # Limpiar checkboxes de bienes en Argentina, recorriendo la lista explicitamente
    for variable in variables_bienes_argentina:
        if variable.get() == True:
            variable.set(False)

    # Limpiar checkboxes de bienes en el exterior, recorriendo la lista explicitamente
    for variable in variables_bienes_exterior:
        if variable.get() == True:
            variable.set(False)