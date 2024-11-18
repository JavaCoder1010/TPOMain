import tkinter as tk


def crear_campos_entrada(ventana, entradas):
    """
    Crea los campos de entrada para el formulario.
    """
    labels = [
        "DNI:",
        "Apellido:",
        "Nombre:",
        "Edad:",
        "Fecha de Nacimiento (dd-mm-aaaa):",
        "Monto:",
        "Fecha de Declaración (dd-mm-aaaa):",
        "Origen de los fondos:",
    ]

    i = 0
    while i < len(labels):
        label = labels[i]
        etiqueta = tk.Label(ventana, text=label, anchor=tk.E, width=30)
        etiqueta.grid(row=i, column=0, sticky=tk.E)
        entry = tk.Entry(ventana, width=30)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entradas.append(entry)
        i += 1
    return i
