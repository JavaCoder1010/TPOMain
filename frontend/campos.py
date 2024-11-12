import tkinter as tk
from tkinter import ttk

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
    
    print("\nCreando campos de entrada:")
    for i, label in enumerate(labels):
        print(f"Creando campo {i}: {label}")
        etiqueta = tk.Label(ventana, text=label, anchor=tk.E, width=30)
        etiqueta.grid(row=i, column=0, sticky=tk.E)
        entry = tk.Entry(ventana, width=30)
        entry.grid(row=i, column=1, padx=5, pady=5)
        entradas.append(entry)
        print(f"Campo {i} creado")
    
    return len(labels)