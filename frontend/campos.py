import tkinter as tk

def crear_campos_entrada(ventana, entradas):
    """
    Crea los campos de entrada para el formulario y los agrega a la ventana principal.

    Args:
        ventana (tk.Tk): La ventana principal de la interfaz.
        entradas (list): La lista que se utiliza para almacenar los EntryField de Tkinter.
    """
    labels = [
        "DNI:",
        "Apellido:",
        "Nombre:",
        "Edad:",
        "Fecha de Nacimiento (dd-mm-aaaa):",
        "Profesión:",
        "Monto:",
        "Fecha de Declaración (dd-mm-aaaa):",
        "Origen de los fondos:",
    ]

    i = 0

    for label in labels:
        etiqueta = tk.Label(ventana, text=label, anchor=tk.E, width=30)
        etiqueta.grid(row=i, column=0, sticky=tk.E)

        entry = tk.Entry(ventana, width=30)
        entry.grid(row=i, column=1, padx=5, pady=5)

        entradas.append(entry)

        i = i + 1
