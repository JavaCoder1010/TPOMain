import tkinter as tk

def crear_checkboxes(ventana, variables_bienes_argentina, variables_bienes_exterior):
    """
    Crea los checkboxes para los bienes en Argentina y en el exterior
    dentro de una ventana dada.

    Args:
        ventana (tk.Tk): La ventana en la que se crearn los checkboxes.
        variables_bienes_argentina (list): La lista de variables BooleanVar que
            se utilizarn para los checkboxes de bienes en Argentina.
        variables_bienes_exterior (list): La lista de variables BooleanVar que
            se utilizarn para los checkboxes de bienes en el exterior.
    """
    frame_checkboxes = tk.Frame(ventana)
    frame_checkboxes.grid(row=0, column=2, rowspan=9, padx=10, pady=5)

    tk.Label(frame_checkboxes, text="Bienes en Argentina:").pack(anchor=tk.W)
    nombres_bienes_argentina = [
        "Moneda",
        "Inmuebles",
        "Acciones y participaciones",
        "Títulos valores",
        "Otros bienes muebles",
        "Créditos",
        "Derechos y bienes intangibles",
        "Criptomonedas y criptoactivos",
        "Otros bienes",
    ]

    for nombre in nombres_bienes_argentina:
        var = tk.BooleanVar()
        variables_bienes_argentina.append(var)
        tk.Checkbutton(frame_checkboxes, text=nombre, variable=var).pack(anchor=tk.W)

    tk.Label(frame_checkboxes, text="Bienes en el exterior:").pack(anchor=tk.W)
    nombres_bienes_exterior = [
        "Moneda extranjera",
        "Inmuebles",
        "Acciones y participaciones",
        "Títulos valores",
        "Otros bienes muebles",
        "Créditos",
        "Derechos y bienes intangibles",
        "Otros bienes",
    ]

    for nombre in nombres_bienes_exterior:
        var = tk.BooleanVar()
        variables_bienes_exterior.append(var)
        tk.Checkbutton(frame_checkboxes, text=nombre, variable=var).pack(anchor=tk.W)